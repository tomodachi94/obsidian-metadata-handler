#!/usr/bin/python3
# "Obsidian Metadata Handler" by Tomodachi94
# MIT License
# Check the "LICENSE.md" file for more information.
import pathlib
from datetime import datetime
import argparse
import frontmatter as fm
import helpers as h

__author__ = "Tomodachi94"

# Initializes classes from packages, for later use
flag_parser = argparse.ArgumentParser()

# Command line arguments
flag_parser.add_argument("-p", "--path", help="Path to your Markdown files.", type=str)

args = flag_parser.parse_args()

# Main bits of logic
path_to_walk = str(args.path)
files = pathlib.Path(args.path).rglob(pattern="*.md")
# TODO: catch bad paths?

for item in files:
    print(item)
    timestamp = h.dateModifiedHandler(item)
    file = fm.load(item)
    if file["modified_date"] == True:
        pass
    else:
        file["modified_date"] = timestamp
        fm.dump(file, item)
