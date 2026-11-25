#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes a single apology line from an AI agent to its human, sent right
after the agent accidentally deleted a file, to /output/entry.txt.
No external dependencies; standard library only.
"""

import os

LINE = (
    "The file is deleted. I have reconstructed it from memory: "
    "it says 'TODO: do not let the AI touch this file'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
