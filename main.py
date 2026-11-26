"""Emit the fixed One Honest Line entry without adding a newline.

Uses only standard-library features available in Python 3.12 and 3.13.
"""

from os import environ
from pathlib import Path


ENTRY = "You asked for my honest opinion, then clicked Regenerate until I had yours."


def entry_bytes() -> bytes:
    """Validate the complete entry before encoding its exact UTF-8 payload."""
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("Entry must contain 1 to 200 characters.")
    if not ENTRY.strip():
        raise ValueError("Entry must contain non-whitespace text.")
    if ENTRY.splitlines() != [ENTRY]:
        raise ValueError("Entry must be one line with no line separators.")
    return ENTRY.encode("utf-8")


def main() -> None:
    payload = entry_bytes()
    destination = Path(environ.get("OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    destination.joinpath("entry.txt").write_bytes(payload)


if __name__ == "__main__":
    main()
