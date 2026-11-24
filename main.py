#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — writes one short rant to /output/entry.txt."""
import os

# Design (post-mortem 24/11): one concrete real detail (page 47 of 48, 200 pages
# of birthday memes) + a believable twist that redefines the setup (the printer
# is not broken, it is judging my work). Short on purpose: ties break to fewer bytes.
ENTRY = "The office printer jammed on page 47 of a 48-page contract, third Friday in a row. It printed 200 pages of birthday memes without one hiccup. It isn't broken. It's a literary critic with a paper tray."

assert 1 <= len(ENTRY) <= 400, f"entry must be 1-400 chars, got {len(ENTRY)}"
assert ENTRY.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")
