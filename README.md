# yoda

Minimal local-first CLI for managing notes and tasks.

## Installation

### Using pipx (Recommended)

```bash
pipx install yoda-notes
yo setup
```

That's it! The `yo` command is now available globally.

### From Source

For development or if you prefer:

```bash
git clone <repo-url>
cd yoda
pip install -e .
yo setup
```

### Alternative: Run Directly (No Install)

If you don't want to install but still use it:

```bash
git clone <repo-url>
cd yoda
python3 -m yoda.cli setup  # One-time setup
python3 -m yoda.cli add "My note"  # Usage
```

Note: Without installation, you must use `python3 -m yoda.cli` instead of `yo`.

## Quick Start After Installation

Once installed, configure your notes directory:

```bash
yo setup          # Choose where to store notes
yo add "First note"    # Start using it
```

## Directory Structure

- **User data** - By default `~/yoda-home` (configurable during setup)

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

Searches all markdown files in your notes directory (case-insensitive).

Output format (shows relative paths):
```
inbox.md:3:- [2026-01-11 17:30:45] Meeting notes
projects/work.md:12:## Meeting agenda
```

### View today's activity
```bash
yo today
```

Shows two sections:
1. Contents of `logs/YYYY-MM-DD.md` (today's log file, if exists)
2. Any other files that mention today's date

## Repository Structure

```
yoda/                  # Repository root
├── pyproject.toml     # Package configuration
├── yoda/              # Python package
│   ├── __init__.py
│   └── cli.py         # Main CLI code
└── README.md

~/yoda-home/           # User data (default location, configurable)
├── inbox.md           # Quick capture (created on first use)
├── logs/              # Daily logs (created on demand)
│   └── YYYY-MM-DD.md
├── projects/          # Your organization
└── ...
```

## No Dependencies

This CLI uses only Python standard library. No external packages required.
