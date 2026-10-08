import base64
import pathlib
import sys

root = pathlib.Path("journal/parts")
out = pathlib.Path("journal")
stems = ["cover", "page-1", "page-2", "page-3", "page-8", "page-51"]
for stem in stems:
    parts = sorted(root.glob(stem + "-*.b64"))
    if not parts:
        sys.exit("missing parts for " + stem)
    text = "".join(p.read_text().strip() for p in parts)
    data = base64.b64decode(text)
    if data[:2] != b"\xff\xd8":
        sys.exit(stem + " is not a jpeg")
    dest = out / (stem + ".jpg")
    dest.write_bytes(data)
    print(dest, len(data))
