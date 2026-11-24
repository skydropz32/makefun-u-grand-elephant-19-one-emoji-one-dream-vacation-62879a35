#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry: a single emoji for a dream vacation.

The emoji: Mount Fuji (🗻) — a snow-capped volcano under a clear sky, the
postcard of a once-in-a-lifetime trip to Japan. One character, no words:
a specific dream destination that reads instantly at any size.
"""

import os

LINE = "🗻"


def validate(line):
    """Enforce the competition gate: 1-8 chars, not only whitespace, one emoji."""
    if not 1 <= len(line) <= 8:
        raise ValueError("entry must be 1-8 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) != 1:
        raise ValueError("entry must be exactly one emoji, got %d chars" % len(line))
    return line


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
