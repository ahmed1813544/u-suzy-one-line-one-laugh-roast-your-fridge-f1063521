#!/usr/bin/env python3
"""Write one original roast line to entry.txt.

Deterministic: the same single line is written on every run, so two
runs produce byte-identical output."""

import os

LINE = "My fridge's crisper drawer is just a vegetable morgue with mood lighting."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
