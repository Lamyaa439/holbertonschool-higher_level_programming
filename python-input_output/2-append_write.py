#!/usr/bin/python3
"""
2-append_write.py modul to appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    this function to appends a string at the end of a text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
