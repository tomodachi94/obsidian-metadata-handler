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
path_to_walk = args.path
path_to_walk = str(path_to_walk)
files = pathlib.Path(args.path).rglob(pattern="*.md")


def dateModifiedHandler(path):
    """
    Gets the created timestamp from the `path` variable.
    """
    file = pathlib.Path(path)
    ctime = datetime.fromtimestamp(file.stat().st_ctime)
    return ctime


for item in files:
    print(item)
    timestamp = h.dateCreatedHandler(item)
    file = fm.load(item)
    file["created_date"] = timestamp
    fm.dump(file, item)
