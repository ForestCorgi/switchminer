#!/usr/bin/env python3

import os

from subprocess import call

os.chdir(os.path.dirname(os.path.realpath(__file__)))

magic_name = "apple.db"
lines = []

with open(magic_name, "r") as magic_db:
    for line in magic_db:
        lines.append(line.strip())

with open(magic_name, "w") as magic_db:
    for line in lines:
        if line == lines[-1]:
            magic_db.write(line)
        else:
            magic_db.write(line + "\n")

call(["file", "-C", "-m", magic_name])
