#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for s in str:
        if index(s) == 3:
            continue
        else:
            new_str += s
    return new_str
