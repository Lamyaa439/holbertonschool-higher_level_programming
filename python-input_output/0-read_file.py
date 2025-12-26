#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        f_contents = f.read()
        print(f_contents, end="")
