# yoda

Minimal local-first CLI for managing notes and tasks.

## Directory Structure

- **`~/Code/yoda`** - Application code (this repository)
- **`~/yoda-home`** - User data (notes, logs, inbox)

## Setup

1. Ensure Python 3.6+ is installed
2. Clone this repository to `~/Code/yoda`
3. Make the CLI executable:
   ```bash
   chmod +x ~/Code/yoda/yo
   ```
4. Add to your PATH by adding this line to `~/.zshrc` or `~/.bashrc`:
   ```bash
   export PATH="$HOME/Code/yoda:$PATH"
   ```
5. Reload your shell:
   ```bash
   source ~/.zshrc  # or source ~/.bashrc
   ```

## Usage

### Add entries to inbox
```bash
yo add "Meeting notes: discussed project timeline"
yo add "TODO: Review pull request"
```

Appends timestamped entries to `~/yoda-home/inbox.md`:
```
- [2026-01-11 17:30:45] Meeting notes: discussed project timeline
```

### Search across all notes
```bash
yo search "meeting"
yo search "TODO"
```

Searches all markdown files in `~/yoda-home` (case-insensitive).

Output format:
```
/Users/kb/yoda-home/inbox.md:3:- [2026-01-11 17:30:45] Meeting notes
/Users/kb/yoda-home/projects/work.md:12:## Meeting agenda
```

### View today's activity
```bash
yo today
```

Shows two sections:
1. Contents of `~/yoda-home/logs/YYYY-MM-DD.md` (today's log file)
2. Any other files that mention today's date

## File Structure

```
~/Code/yoda/
├── yo                 # Main executable
├── requirements.txt   # Empty (stdlib only)
└── README.md          # This file

~/yoda-home/           # User data directory (managed by you)
├── inbox.md          # Quick capture
├── logs/
│   └── YYYY-MM-DD.md # Daily logs
├── projects/         # Project notes
└── ...               # Your organization
```

## No Dependencies

This CLI uses only Python standard library. No external packages required.
