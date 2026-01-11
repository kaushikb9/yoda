Reset context.

Project layout is strictly separated:
	•	Code lives in ~/Code/yoda (this repo)
	•	Notes/data live in ~/yoda-home

You are not allowed to create, move, or modify files in ~/yoda-home except appending content to markdown files when explicitly instructed.

We are building a real, extensible CLI app called yoda, invoked as yo.

Implementation constraints:
	•	Use Python
	•	No bash scripts except a thin launcher if required
	•	No auto-scaffolding
	•	No PRD usage
	•	No AI features

Task (only this):
	•	Create a minimal Python-based CLI (yo) that supports:
	•	yo add "text" → append timestamped entry to ~/yoda-home/inbox.md
	•	yo search "query" → local search across ~/yoda-home
	•	yo today → list today's log file
	•	Keep the code small and boring
	•	Stop after implementation and explain the file structure

Ask before doing anything else.
