"""The One-Liner Groan-Off entry.

Writes a single original one-line dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: no network, no randomness, no clock, no environment-dependent
output. The file holds exactly the joke, no trailing newline.
"""

import os

JOKE = "I told the yogurt it was sour. It said, 'I'm cultured, not sour.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
