#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    value = 0
    upper_value = 0
    for s in str:
        value = ord(s)
        if 97 <= value <= 122:
            upper_value = value - 32
            upper_str += chr(upper_value)
        else:
            upper_str += s
    print("{}".format(upper_str))


