#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    str_len = len(str)
    for i in range(str_len):
        if i == n:
            continue
        else:
            new_str += str[i]
    return new_str
