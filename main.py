#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt. Fully deterministic: no network, no randomness,
no clock, no environment input. The line is 145 characters.
"""

import os

LINE = (
    "One star. The mailman comes every day, taunts me through the window, "
    "and leaves. I have barked at him 412 times. He is not afraid. "
    "I am not okay."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back verification: the file on disk must be exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "read-back mismatch in /output/entry.txt"
    print(f"Wrote {len(written)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
