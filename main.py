"""One-line excuse an AI agent gives for a missed deadline.

The line is delivered deadpan, in the agent's own voice, growing out of
its own machinery: the context window evicting the deadline to make room
for the error logs of the previous miss. The laugh lands late, in the
final words, with nothing explained after them. The line is 110
characters, so line plus trailing newline stays well within the 200
character gate.
"""

# Verified by read-back: 110 characters, one line, so line + trailing
# newline = 111 bytes — inside the 200-character gate.
LINE = "My context window evicted the deadline to make room for the error logs from the last time I missed a deadline."

import os


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    text = LINE
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
