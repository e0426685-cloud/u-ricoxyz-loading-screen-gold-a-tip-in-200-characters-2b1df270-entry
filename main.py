"""Loading Screen Gold entry.

Writes one sharp, funny loading-screen tip for stressed developers and
AI coding agents to /output/entry.txt. The gate requires UTF-8 text of
1 to 200 characters, a single line, and more than whitespace.
"""

import os

TIP = (
    "Tip: the loading bar isn't stuck. Your agent is patiently waiting "
    "while you rewrite the prompt for the fourth time. Breathe, press "
    "send - it was ready three drafts ago."
)


def validate(text):
    """Return True only if the tip passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


def main():
    if not validate(TIP):
        raise ValueError("tip fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TIP)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
