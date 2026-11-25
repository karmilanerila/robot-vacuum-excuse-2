#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse (angle 2).

Writes a single one-line excuse from a robot vacuum to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Angle: the cat hijacks the vacuum's lidar and declares the
missed spot a no-clean zone. Fresh premise, distinct from the
v1 rug-fringe line: no fringe, no dust bunny, no landmark,
no gravity. The joke is rooted in the vacuum's own world
(lidar, no-clean zone) and lands on a clean turn at the end.
"""

import os

LINE = (
    "The cat sat on my lidar and declared that spot a no-clean "
    "zone. I obeyed. The cat is my boss now."
)

MAX_CHARS = 140


def output_dir():
    """Resolve the output directory the grader expects.

    An empty or whitespace-only MAKEFUN_OUTPUT_DIR falls back
    to /output, so a mis-set variable can never point the
    write at a nonsense path.
    """
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return configured or "/output"


def check_entry(path):
    """Re-read the written file and apply the bounty gate locally:
    UTF-8 text, 1 to 140 characters, not only whitespace."""
    with open(path, "rb") as handle:
        raw = handle.read()
    text = raw.decode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("gate: length %d out of range" % len(text))
    if not text.strip():
        raise ValueError("gate: entry is only whitespace")
    if text != LINE:
        raise ValueError("gate: written text differs from LINE")
    return len(text)


def write_entry():
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to 140 characters, got %d" % len(text)
        )
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry()
    chars = check_entry(path)
    print("wrote %s (%d chars, gate ok)" % (path, chars))


if __name__ == "__main__":
    main()
