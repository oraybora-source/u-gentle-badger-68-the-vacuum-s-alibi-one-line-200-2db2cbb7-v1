"""The Vacuum's Alibi: write one deadpan excuse to /output/entry.txt.

The line was written in this session for the make.fun bounty
u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.
Deterministic: same bytes on every run. No network, no input files.
"""

import os

ENTRY = (
    "Sensor log 04:12 \u2014 I did not miss it. I reclassified the crumb "
    "as floor d\u00e9cor after a 0.4-second sensor vote, 2\u20131, "
    "with my battery abstaining."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The gate reads the file as any user; make it world-readable.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
