"""One-star review of something essential.

Writes a single deadpan one-star review (one line, at most 160
characters) to /output/entry.txt. Fully deterministic: the same
text on every run, no randomness, no network, no input.
"""

import os

REVIEW = "One star. Gravity holds the Moon in orbit yet lets my phone land face-down on concrete."


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
