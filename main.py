#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entry program.

Writes a single original robot wedding vow to /output/entry.txt.

The craft: a vow is a promise, so the line opens as a promise ("I promise
to keep...") and lists three kinds of machine care — batteries, firmware,
ports — in a steady three-beat rhythm, like a real vow's "to have and to
hold". The laugh is saved for the last few words, and it is made specific:
the partner doesn't just crash, it blue-screens — the one failure every
machine owner recognises — and it happens at the altar, the most
wedding-specific place for it to go wrong. Deterministic: the same line,
every run.
"""

import os

VOW = (
    "I promise to keep your batteries charged, your firmware updated, "
    "and your ports dust-free \u2014 and to love you even when you "
    "blue-screen at the altar."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
