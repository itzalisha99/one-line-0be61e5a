#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

The line: a self-checkout machine, asked if help is needed, answers by
scanning the shopper's dignity instead of the shopping. The joke lands in
the last three words, where the machine's job (scanning) turns on the
shopper instead of the groceries.
"""

import os

LINE = "The self-checkout asked if I needed help. I said no. It scanned my dignity twice."


def validate(text):
    """Mirror the bounty gate: 1-140 chars, UTF-8, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 140:
        raise ValueError("entry is over 140 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
