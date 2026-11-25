"""The 4AM Commit: Funniest Agent Bug-Fix Message.

One program, one job: write the single commit message an AI agent
leaves in the log after a long night of chasing down and fixing its
own bugs. The message is fixed text, chosen before the run, so the
program is fully deterministic: no clock, no randomness, no network,
no input. It writes the message to ``entry.txt`` inside the output
directory the sandbox provides (``MAKEFUN_OUTPUT_DIR``, ``/output``
in the grader), which is the file the gate scorer reads.
"""

import os

COMMIT_MESSAGE = (
    "fix: the bug was me. all 47 commits of it. "
    "I have reviewed my own work and I am pressing charges"
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def build_entry() -> str:
    """Return the commit message, exactly as it goes in the log.

    The gate scorer only judges a text of 1 to 200 characters, so a
    message outside that range is refused here instead of emitted:
    a program that can only ever write a valid entry cannot fail
    the gate by accident.
    """
    message = COMMIT_MESSAGE
    if not 1 <= len(message) <= 200 or not message.strip():
        raise ValueError(
            f"commit message must be 1-200 non-blank characters, got {len(message)}"
        )
    return message


def main() -> None:
    message = build_entry()
    print(message)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as handle:
        handle.write(message)


if __name__ == "__main__":
    main()
