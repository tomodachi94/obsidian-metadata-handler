# "Obsidian Metadata Handler" by Tomodachi94
# MIT License
# Check the "LICENSE.md" file for more information.
import pathlib
from datetime import datetime

__author__ = "Tomodachi94"
def dateModifiedHandler(path):
    """
    Gets the file modified timestamp from the `path` variable.
    """
    file = pathlib.Path(path)
    mtime = datetime.fromtimestamp(file.stat().st_mtime)
    return mtime

def dateCreatedHandler(path):
    """
    Gets the file created timestamp from the `path` variable.
    """
    file = pathlib.Path(path)
    ctime = datetime.fromtimestamp(file.stat().st_ctime)
    return ctime