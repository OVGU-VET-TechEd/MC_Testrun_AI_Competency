#!/usr/bin/env python3
"""Combine LiaScript module files (M[0-9]*.md) into one course file for a single SCORM package.

Usage: python3 combine_modules.py <course_folder> <output.md> "<course title>"

Keeps the LiaScript header (<!-- ... -->) of the first module, replacing its comment line
with the course title; strips the headers of all other modules. Module "# " headings stay
level 1, so every module becomes a top-level section in the LiaScript table of contents.
"""
import re
import sys
from pathlib import Path

HEADER = re.compile(r"\A\s*<!--.*?-->\s*", re.S)


def main():
    folder, out, title = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    files = sorted(folder.glob("M[0-9]*.md"))
    parts = []
    for n, f in enumerate(files):
        text = f.read_text(encoding="utf-8")
        header = HEADER.match(text)
        body = text[header.end():] if header else text
        if n == 0 and header:
            head = re.sub(r"^comment:.*$", f"comment:  {title}", header.group(0).strip(), flags=re.M)
            parts.append(head + "\n\n")
        parts.append(body.strip() + "\n\n")
    out.write_text("".join(parts), encoding="utf-8")
    print(f"wrote {out} from {len(files)} modules")


if __name__ == "__main__":
    main()
