# yoda (`yo`)

`yoda` is a **local-first, minimal CLI** for capturing thoughts, todos, and simple notes in plain Markdown files.

The goal is utility first — **your files remain yours** — with no heavy structure or hidden databases.  
AI and automation are *explicit and opt-in*.

---

## Why this exists

Most note/todo tools either:

- enforce rigid structure, or  
- hide your files in opaque databases, or  
- auto-organize in ways you don’t control

`yoda` tries a different path:  
**lean, predictable, and file-centric**.

You can always edit, move, and manage your notes manually without breaking anything.

---

## Core principles

- **Local-first** — data lives on your filesystem.  
- **Markdown as source of truth** — you can edit files directly.  
- **Minimal and boring** — no databases, no sync, no hidden logic.  
- **Explicit AI** — nothing uses AI unless you ask.  
- **Trust over features** — CLI shouldn’t surprise you.

These principles guide design and future additions.

---

## Current status (Phase 1)

Phase 1 is all about basic capture and retrieval.

Basic commands are supported:

```
yo add "some thought or todo"
yo search "keyword"
yo today
```

## Installation

### Method 1: pipx (Recommended for most users)

**Best for:** Global installation without conflicts

```bash
pipx install yoda-notes
yo setup
```

The `yo` command is now available globally. pipx automatically handles PATH configuration.

### Method 2: From Source with Virtual Environment (Recommended for development)

**Best for:** Development or testing changes locally

```bash
git clone <repo-url>
cd yoda

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode
pip install -e .

# Use yo (only while venv is activated)
yo setup
```

**Important:** You must activate the venv (`source venv/bin/activate`) each time you open a new terminal to use the `yo` command.

### Method 3: System-wide Installation from Source

**Best for:** System-wide access without venv activation

```bash
git clone <repo-url>
cd yoda
pip install --user -e .
```

**Troubleshooting:** If `yo` command is not found after installation:

```bash
# Check where yo was installed
python3 -m site --user-base

# Add to your ~/.zshrc or ~/.bashrc:
export PATH="$(python3 -m site --user-base)/bin:$PATH"

# Reload shell
source ~/.zshrc  # or ~/.bashrc
```

**Note:** Using pipx (Method 1) avoids this PATH issue entirely.

### Method 4: Run Directly (No Install)

**Best for:** Quick testing without installation

```bash
git clone <repo-url>
cd yoda
python3 -m yoda.cli setup  # One-time setup
python3 -m yoda.cli add "My note"  # Usage
```

With this method, use `python3 -m yoda.cli` instead of `yo` for all commands.

## Quick Start After Installation

Once installed, configure your notes directory:

```bash
# If using venv (Method 2), activate first:
source venv/bin/activate

# Run setup and start using
yo setup                # Choose where to store notes
yo add "First note"     # Start using it
```

## Directory Structure

- **User data** - By default `~/yoda-home` (configurable during setup)

## Usage

**Note:** If you installed using Method 2 (venv), make sure to activate it first: `source venv/bin/activate`

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
