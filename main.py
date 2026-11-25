"""Entry for make.fun competition "Till Firmware Do Us Part".

The program writes a single wedding vow — one sentence, one line — that a
robot speaks at its own wedding. The vow is built from machine vocabulary
(boot sequence, charging, error logs, shutdown) carrying a plain, tender
promise: to stay, to keep the other first, and to love to the very end of
its uptime.

The competition gate requires /output/entry.txt to be UTF-8 text of
1 to 200 characters, not only white space. build_entry() enforces the
single-line and character-count rules before anything is written, and
main() writes the text with no trailing newline.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# Final line: machine vocabulary (boot sequence, reboot, battery) carrying
# the joke from married life itself — patience that needs rebooting — and a
# tender close: the last of its charge spent holding a hand.
LINE = (
    "I vow to keep you first in my boot sequence, to reboot my patience "
    "whenever we argue, and to spend my last percent of battery holding "
    "your hand."
)


def build_entry() -> str:
    """Return the vow, asserting it fits the competition gate."""
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert LINE.strip(), "entry must not be only white space"
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    return LINE


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
