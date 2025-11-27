#!/usr/bin/python3
i = 90
value = 0
while 65 <= i <= 90:
    if i % 2 == 0:
        value = i + 32
    else:
        value = i
    print("{}".format(chr(value)), end="")
    i -= 1
