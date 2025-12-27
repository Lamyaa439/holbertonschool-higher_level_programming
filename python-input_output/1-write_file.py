#!/usr/bin/python3
"""
1-write_file.py moduls to write a file
"""


def write_file(filename="", text=""):
    """
    this function to write in the file
    """
    with open(filename, "w") as f:
        return f.write(text)
