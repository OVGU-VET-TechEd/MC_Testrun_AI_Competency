#!/usr/bin/env python3
"""Check a LiaScript micro-credential course folder.

Usage: python3 check_course.py <course_folder>

Checks per module file (M[0-9]*.md):
  * sum of page time estimates ("> ⏱ 20 min" / "> ⏱ 1.5 hours") vs. the module total
    stated in the first heading block ("> ⏱ **4 hours**")
  * balanced quiz solution blocks (lines of >= 10 asterisks must come in pairs)
  * runnable code blocks: every ```js block is followed by <script>@input</script>
  * anthropomorphism lint: mental/intentional verbs, for manual review
Overall: grand total of module totals (should equal the ECTS workload, 30 h per ECTS).
"""
import re
import sys
from pathlib import Path

LINT = re.compile(r"\b(thinks?|knows?|understands?|believes?|wants?|lies|lied|lying|"
                  r"admits?|decides?|decided|remembers?|realises?|refuses?|confused)\b",
                  re.I)


def minutes(text):
    m = re.search(r"([\d.]+)\s*(min|hour|h\b)", text)
    if not m:
        return 0
    v = float(m.group(1))
    return v if m.group(2) == "min" else v * 60


def check(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    total, pages, stars, lint = None, 0.0, 0, []
    for i, line in enumerate(lines, 1):
        if line.startswith("> ⏱ **") and total is None:
            total = minutes(line)
        elif line.startswith("> ⏱ "):
            pages += minutes(line)
        if re.fullmatch(r"\*{10,}", line.strip()):
            stars += 1
        if line.strip().startswith("```js"):
            j = i
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            nxt = lines[j + 1].strip() if j + 1 < len(lines) else ""
            if nxt != "<script>@input</script>":
                print(f"  ! {path.name}:{i} js block not runnable (no <script>@input</script>)")
        for m in LINT.finditer(line):
            lint.append((i, m.group(0)))
    flag = "OK " if total and abs(total - pages) <= 10 else "!! "
    print(f"{flag}{path.name}: stated {total/60 if total else 0:.2f} h, pages {pages/60:.2f} h")
    if stars % 2:
        print(f"  ! {path.name}: unbalanced solution blocks ({stars} star lines)")
    return (total or 0), lint


def main():
    folder = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    grand, all_lint = 0, {}
    for f in sorted(folder.glob("M[0-9]*.md")):
        t, lint = check(f)
        grand += t
        all_lint[f.name] = lint
    print(f"\nGrand total: {grand/60:.2f} h ({grand/60/30:.2f} ECTS)")
    print("\nAnthropomorphism lint (review: deliberate examples are fine):")
    for name, hits in all_lint.items():
        words = ", ".join(f"{w}@{i}" for i, w in hits)
        print(f"  {name}: {len(hits)} hits  {words[:300]}")


if __name__ == "__main__":
    main()
