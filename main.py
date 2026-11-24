"""One-star review of something essential (make.fun).

Writes a single deadpan one-star review, 160 characters or fewer,
to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "One star. Oxygen is free, invisible and everywhere, yet I still "
    "run out of it climbing a single flight of stairs."
)


def main() -> None:
    # Sealed-gate self-check: entry.txt must be UTF-8 text of 1 to 160
    # characters, not only whitespace. Fail loudly instead of shipping
    # an invalid entry.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "!" not in ENTRY, "deadpan: no exclamation marks doing the work"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
