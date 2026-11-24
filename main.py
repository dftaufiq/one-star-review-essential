"""One-star review of something essential (round 2 resubmit).

Writes a single deadpan one-star review (one line, at most 160
characters) to /output/entry.txt. Fully deterministic: the same
text on every run, no randomness, no network, no input, no
environment secrets.

Round 2 replaces the round 1 entry (gravity / phone face-down),
which finished round 1 at rank #871 of 2,248, below the interim
cut of 500, so its score is frozen and only a new entry can move
up. This line is a different subject and a different joke: the
sun blinding the driver on the way home.
"""

import os

# 108 chars / 108 bytes (ASCII) — the bytes tie-break favours short texts,
# and 108 keeps the full 2-beat scene + reveal with nothing to cut.
REVIEW = "One star. The sun sets at exactly 5:47, directly into my windscreen, every single evening on the drive home."


def main():
    # The gate rejects anything over 160 characters, multi-line, or blank;
    # fail loudly here instead of shipping an invalid entry.
    assert 1 <= len(REVIEW) <= 160, f"review is {len(REVIEW)} chars"
    assert "\n" not in REVIEW and REVIEW.strip() == REVIEW
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
