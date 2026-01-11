# Agent Instructions for Claude Code

## Project Layout

Project layout is strictly separated:
- **Code lives in `~/Code/yoda`** (this repository)
- **Notes/data live in `~/yoda-home`** (user data directory)

## File Modification Rules

You are NOT allowed to create, move, or modify files in `~/yoda-home`.

The only exception: the `yo add` command programmatically appends to `~/yoda-home/inbox.md`. This is not something you do directly - the Python code does it when the user invokes the command.

## What You Can Do

- Read any files in `~/yoda-home` to answer questions
- Modify code in `~/Code/yoda`
- Run `yo` commands for testing (which may append to files as designed)
- Search through `~/yoda-home` when testing `yo search`
- Read from `~/yoda-home/logs/` when testing `yo today`

## What You Cannot Do

- Create new files in `~/yoda-home` using tools like Write or Bash
- Move files in `~/yoda-home`
- Modify existing content in `~/yoda-home` using tools like Edit
- Auto-scaffold directories or files in `~/yoda-home`
- Reorganize or refactor user's notes
- Manually append to `~/yoda-home/inbox.md` (only the `yo add` command does this)
