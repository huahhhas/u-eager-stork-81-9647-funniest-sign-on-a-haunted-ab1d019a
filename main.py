"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign (120 chars max) to /output/entry.txt
and prints the same line to stdout.
"""

import os

LINE = "DO NOT REBOOT THE GHOST. It has had 100% uptime since 1987 and it is very proud of that."

# Gate: entry must be 1-120 UTF-8 characters, not only whitespace.
assert 1 <= len(LINE) <= 120 and LINE.strip(), "line must be 1-120 chars"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
