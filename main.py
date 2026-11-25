#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — make.fun entry.

Writes one funny one-line review of a doorstop to /output/entry.txt.
The review is a fixed, hand-written line: the program is
deterministic, uses only the standard library, and always produces
the exact same output on every run.

The joke: a doorstop's entire job really is lying on the floor, so
the review treats it as the most loyal employee in the house — it
has never called in sick, never asked for a raise, and never once
let the door slam. The dullness itself is the punchline.
"""

import os

# The entry: one line, no trailing newline, well under the
# 200-character gate (checked again at write time).
REVIEW = (
    "My doorstop's entire job is lying on the floor, and it has "
    "still never once called in sick, asked for a raise, or let "
    "the door slam."
)

MAX_CHARS = 200


def main() -> None:
    line = REVIEW.strip()
    if not line:
        raise SystemExit("review is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"review is {len(line)} chars, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("review must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Round-trip check: what the grader reads must be exactly the
    # line above, one line, within the limit, no trailing newline.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip mismatch in entry.txt")


if __name__ == "__main__":
    main()
