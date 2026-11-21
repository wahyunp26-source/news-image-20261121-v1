#!/usr/bin/env python3
"""news-image-20261121 v1 entrypoint (Python 3.13, stdlib only).

Copies entry.png (shipped beside this file) into $MAKEFUN_OUTPUT_DIR
(default /output) and verifies the copy is byte-identical to the source.
No network, no third-party packages, deterministic: the same bytes out
on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        print("missing entry.png beside main.py", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(SRC, "rb") as f:
        src_bytes = f.read()
    with open(DST, "rb") as f:
        dst_bytes = f.read()
    if src_bytes != dst_bytes:
        print("copy differs from source", file=sys.stderr)
        return 1
    print(f"wrote {DST} ({len(dst_bytes)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
