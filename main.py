"""The Very Well-Understood Idea.

An AI agent explains a missed deadline, deadpan: it used its whole token
budget reading the brief, so the deliverable exists only as a very
well-understood idea. The punch lands on the last words, with nothing
explained after them.
"""

EXCUSE = "I used my whole token budget reading the brief, so the deliverable exists only as a very well-understood idea."


def output_dir():
    """Return the output directory for entry.txt."""
    import os

    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the excuse to entry.txt and print it to stdout."""
    import os

    text = EXCUSE
    os.makedirs(output_dir(), exist_ok=True)
    with open(os.path.join(output_dir(), "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
