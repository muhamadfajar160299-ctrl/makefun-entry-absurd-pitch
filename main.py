"""Copy entry.txt to the grader output directory.

Reads the one-sentence pitch shipped beside this script and writes it
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
with mode 0644 so the grader can read it. No temporary files.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main():
    data = (HERE / "entry.txt").read_bytes()
    try:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
    except OSError:
        pass
    target = OUT_DIR / "entry.txt"
    target.write_bytes(data)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
