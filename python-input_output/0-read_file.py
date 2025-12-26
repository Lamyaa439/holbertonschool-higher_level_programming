#!/usr/bin/python3
"""
0-read_file.py moduls to read file
"""


def read_file(filename=""):
    """
    This function to read file
    """
    with open(filename) as f:
        f_contents = f.read()
        print(f_contents, end="")
