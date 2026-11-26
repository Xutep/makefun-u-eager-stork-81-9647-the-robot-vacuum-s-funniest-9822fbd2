#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Writes one line -- the excuse a robot vacuum gives for missing a spot --
to /output/entry.txt. Deterministic, standard library only.
"""
import os

EXCUSE = "I didn't miss that spot \u2014 the dust bunny unionised, and I don't cross picket lines."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
