#!/usr/bin/env python3

import os

from subprocess import call

lines = []

os.chdir("plugins")

with open("magic.db", "r") as magic_db:
    for line in magic_db:
        stripped = line.strip()
        if stripped != "":
            lines.append(stripped)

with open("magic.db", "w") as magic_db:
    for line in lines:
        magic_db.write(line)

call(["file", "-C", "-m", "magic.db"])
