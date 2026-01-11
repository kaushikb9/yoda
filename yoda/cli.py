import os
import sys
from pathlib import Path
from datetime import datetime


def get_yoda_home():
    """Get yoda-home directory path."""
    yoda_home = os.environ.get('YODA_HOME')
    return Path(yoda_home) if yoda_home else Path.home() / 'yoda-home'


def cmd_add(text):
    """Append timestamped entry to inbox.md."""
    yoda_home = get_yoda_home()

    if not yoda_home.exists():
        print(f"Error: {yoda_home} does not exist.\n", file=sys.stderr)
        print("Run setup first:", file=sys.stderr)
        print("  yo setup", file=sys.stderr)
        sys.exit(1)

    inbox = yoda_home / 'inbox.md'

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"- [{timestamp}] {text}\n"

    with open(inbox, 'a') as f:
        f.write(entry)

    print("Added to inbox.md")


def cmd_search(query):
    """Search for query across all markdown files."""
    yoda_home = get_yoda_home()

    if not yoda_home.exists():
        print(f"Error: {yoda_home} does not exist.\n", file=sys.stderr)
        print("Run setup first:", file=sys.stderr)
        print("  yo setup", file=sys.stderr)
        sys.exit(1)

    query_lower = query.lower()
    found = False

    for md_file in sorted(yoda_home.rglob('*.md')):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    if query_lower in line.lower():
                        rel_path = md_file.relative_to(yoda_home)
                        print(f"{rel_path}:{line_num}:{line.rstrip()}")
                        found = True
        except Exception as e:
            print(f"Warning: Could not read {md_file.relative_to(yoda_home)}: {e}", file=sys.stderr)
            continue

    if not found:
        print("No matches found.")


def cmd_today():
    """Show today's log file and mentions of today's date in other files."""
    yoda_home = get_yoda_home()

    if not yoda_home.exists():
        print(f"Error: {yoda_home} does not exist.\n", file=sys.stderr)
        print("Run setup first:", file=sys.stderr)
        print("  yo setup", file=sys.stderr)
        sys.exit(1)

    today = datetime.now().strftime('%Y-%m-%d')
    today_log = yoda_home / 'logs' / f'{today}.md'

    # Part A: Show today's log file
    print(f"=== Today's log ({today}) ===\n")
    if today_log.exists():
        with open(today_log, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip():
                print(content)
            else:
                print("No log file for today")
    else:
        print("No log file for today")

    # Part B: Search for today's date in other files
    print(f"\n=== Other mentions of {today} ===\n")
    found = False

    for md_file in sorted(yoda_home.rglob('*.md')):
        # Skip today's log file
        if md_file == today_log:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    if today in line:
                        rel_path = md_file.relative_to(yoda_home)
                        print(f"{rel_path}:{line_num}:{line.rstrip()}")
                        found = True
        except Exception as e:
            rel_path = md_file.relative_to(yoda_home)
            print(f"Warning: Could not read {rel_path}: {e}", file=sys.stderr)
            continue

    if not found:
        print("No other mentions found.")


def _is_installed():
    """Check if yoda is installed via pip/pipx (not running from source)."""
    # Check if being run via an installed entry point (command in bin/)
    # sys.argv[0] will be like /path/to/bin/yo when installed
    argv0 = str(Path(sys.argv[0]).resolve())
    if '/bin/yo' in argv0 or '\\Scripts\\yo' in argv0:  # Unix or Windows
        return True

    # Also check file location as fallback
    file_path = str(Path(__file__).resolve())
    return 'site-packages' in file_path or '.local' in file_path


def cmd_setup():
    """Interactive setup for yoda."""
    print("=== Yoda Setup ===\n")

    # Get notes directory
    default_home = str(Path.home() / 'yoda-home')
    notes_dir = input(f"Where should yoda store your notes? [{default_home}]: ").strip()
    if not notes_dir:
        notes_dir = default_home

    notes_path = Path(notes_dir).expanduser()

    # Create directory
    try:
        notes_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created {notes_path}")
    except Exception as e:
        print(f"Error: Could not create {notes_path}: {e}", file=sys.stderr)
        sys.exit(1)

    # Check if installed via pip/pipx
    installed = _is_installed()

    if installed:
        # Installed via pip/pipx - PATH is automatic, only configure YODA_HOME if needed
        if notes_dir != default_home:
            print(f"\n=== Environment Configuration ===\n")
            print(f"Add this to your shell config (~/.zshrc or ~/.bashrc):\n")
            print(f'  export YODA_HOME="{notes_path}"\n')
            print("Then reload your shell:")
            print("  source ~/.zshrc\n")

        print("=== Setup Complete ===\n")
        print("Start using yoda:")
        print('  yo add "My first note"')
        print('  yo search "note"')
        print('  yo today')
        return

    # Running from source - need to configure PATH
    yo_dir = Path(__file__).parent.absolute()

    # Detect shell
    shell = os.environ.get('SHELL', '')
    if 'zsh' in shell:
        shell_name = 'zsh'
        config_file = Path.home() / '.zshrc'
    elif 'bash' in shell:
        shell_name = 'bash'
        # Try .bashrc first, then .bash_profile
        bashrc = Path.home() / '.bashrc'
        bash_profile = Path.home() / '.bash_profile'
        config_file = bashrc if bashrc.exists() else bash_profile
    else:
        shell_name = 'unknown'
        config_file = None

    print(f"\n=== Shell Configuration ===\n")
    print(f"Detected: {shell_name} ({config_file})\n")

    # Prepare lines to add
    lines_to_add = []
    lines_to_add.append("# Yoda CLI")
    lines_to_add.append(f'export PATH="{yo_dir}:$PATH"')

    # Only add YODA_HOME if non-default
    if notes_dir != default_home:
        lines_to_add.append(f'export YODA_HOME="{notes_path}"')

    print("To use 'yo' from anywhere, add these lines to your shell config:\n")
    for line in lines_to_add:
        print(f"  {line}")
    print()

    if config_file and config_file.exists():
        # Check if already configured
        try:
            with open(config_file, 'r') as f:
                content = f.read()
                if '# Yoda CLI' in content or str(yo_dir) in content:
                    print("⚠️  Looks like yoda is already configured in your shell config.")
                    print("   Skipping automatic configuration to avoid duplicates.\n")
                    return
        except Exception:
            pass

        response = input("Add automatically? [y/N]: ").strip().lower()
        if response == 'y':
            try:
                with open(config_file, 'a') as f:
                    f.write('\n')
                    for line in lines_to_add:
                        f.write(line + '\n')
                print(f"✓ Updated {config_file}\n")
            except Exception as e:
                print(f"Error: Could not update {config_file}: {e}", file=sys.stderr)
                print("Please add the lines manually.\n")
                sys.exit(1)
        else:
            print("Please add the lines manually to your shell config.\n")
    else:
        print("Could not detect shell config file. Please add the lines manually.\n")

    print("⚠️  Reload your shell to activate:")
    print(f"  source {config_file if config_file else '~/.zshrc'}\n")
    print("Or just open a new terminal window.\n")
    print("=== Setup Complete ===\n")
    print("Test it out:")
    print('  yo add "My first note"')
    print('  yo search "note"')
    print('  yo today')


def print_usage():
    """Print usage information."""
    print("yoda - minimal local-first CLI")
    print()
    print("Usage:")
    print('  yo setup            Interactive setup (first time)')
    print('  yo add "text"       Append timestamped entry to inbox.md')
    print('  yo search "query"   Search across notes directory')
    print('  yo today            Show today\'s log and mentions')


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]

    if command == 'setup':
        cmd_setup()

    elif command == 'add':
        if len(sys.argv) < 3:
            print('Usage: yo add "text"')
            sys.exit(1)
        cmd_add(' '.join(sys.argv[2:]))

    elif command == 'search':
        if len(sys.argv) < 3:
            print('Usage: yo search "query"')
            sys.exit(1)
        cmd_search(' '.join(sys.argv[2:]))

    elif command == 'today':
        cmd_today()

    else:
        print_usage()
        sys.exit(1)


if __name__ == '__main__':
    main()
