#!/usr/bin/env python3
"""One Word From Grandma entry.

Writes exactly one original word -- the word a grandma would text
about AI -- to /output/entry.txt.

The word: Frankenstein. A grandma's classic shorthand for science
gone too far: warm, a little baffled, and funny in a single word,
with no caption needed. She has watched scientists play God on
the telly for sixty years; the moment a grandchild shows her a
machine that talks back, one word leaves her phone: Frankenstein.
"""

import os

WORD = "Frankenstein"


def _check_gate(word: str) -> None:
    """Mirror the sealed gate scorer: UTF-8 text of 1 to 30 characters,
    not only white space, and exactly one word (no spaces at all)."""
    if not (1 <= len(word) <= 30):
        raise ValueError(f"word must be 1-30 characters, got {len(word)}")
    if not word.strip():
        raise ValueError("word must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry must be letters only, no punctuation tricks")


def main() -> None:
    _check_gate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
