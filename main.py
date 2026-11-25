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


MIN_LENGTH = 1
MAX_LENGTH = 159
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry length {len(text)} outside {MIN_LENGTH}..{MAX_LENGTH}"
        )
    if not text.strip():
        raise ValueError("entry must not be blank")
    return text


def main() -> None:
    entry = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(entry)


if __name__ == "__main__":
    main()
