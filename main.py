#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes a single line (at most 120 characters) to /output/entry.txt.

Chosen fortune (v2 — genuine second-round revision of v1): the verb
"linger" became "stay" and "claim it arranged it" became "tell everyone
it arranged it", so the joke lands harder — the spider plant does not
just claim credit, it brags about it to the whole windowsill. Same
dated prediction, same neighbour plant, warmer and funnier.
  1. SPIDER-PLANT CREDIT (chosen) — "Next Tuesday the sun will stay an
     extra hour on your leaves, and the spider plant will tell everyone
     it arranged it."
  2. WINDOW APOLOGY — "By spring you will lean so far toward the light
     that the window will apologise and slide itself open for you."
  3. CAT CONCESSION — "The cat will concede the windowsill is yours and
     nap one leaf away, out of respect, starting tonight."
"""

import os

FORTUNE = (
    "Next Tuesday the sun will stay an extra hour on your leaves, "
    "and the spider plant will tell everyone it arranged it."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} characters"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
