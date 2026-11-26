#!/usr/bin/env python3
"""One-line excuse for skipping a pointless meeting.

Writes a single sharp, relatable excuse to /output/entry.txt
(via MAKEFUN_OUTPUT_DIR), UTF-8, one line, at most 200 characters.
"""

import os

TEXT = (
    "Sorry, I can't join - my calendar just booked me into an emergency "
    "meeting with myself about why I keep saying yes to meetings like this one. "
    "It's running over."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
