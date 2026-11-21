#!/usr/bin/env python3
"""SOLARLUX — catalogue photo of an impossible gadget.

Writes the studio catalogue photograph of a solar-powered flashlight
(a torch that only works in sunlight, so its one accessory is a pair
of sunglasses) to /output/entry.png.

The photograph ships as photo.png next to this program: a 1024x1024
PNG, 362,267 bytes, well inside the gate (<=1,048,576 bytes,
<=1024x1024 px). This program only copies those bytes into place
and makes the output world-readable; it needs no network and no
third-party packages, so it runs in the sandbox as-is.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "photo.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")

MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"missing bundled photograph: {SOURCE}", file=sys.stderr)
        return 1

    with open(SOURCE, "rb") as handle:
        header = handle.read(len(PNG_MAGIC))
        ihdr = handle.read(25)
    if header != PNG_MAGIC:
        print("bundled photograph is not a PNG", file=sys.stderr)
        return 1
    if len(ihdr) < 25 or ihdr[4:8] != b"IHDR":
        print("bundled photograph has no IHDR chunk", file=sys.stderr)
        return 1
    width, height = struct.unpack(">II", ihdr[8:16])
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"bundled photograph too large: {width}x{height}", file=sys.stderr)
        return 1

    size = os.path.getsize(SOURCE)
    if size > MAX_BYTES:
        print(f"bundled photograph too large: {size} bytes", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    os.chmod(OUTPUT_DIR, 0o755)
    os.chmod(OUTPUT, 0o644)

    written = os.path.getsize(OUTPUT)
    print(f"wrote {OUTPUT} ({written} bytes, {width}x{height} PNG)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
