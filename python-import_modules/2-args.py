#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_list = sys.argv
    len_list = len(arg_list)
    name = "argument"
    if len_list > 2:
        name += "s"
    print("{} {}:".format(name, len_list - 1))
    for i in range(1, len_list):
        print("{}: {}".format(i, arg_list[i]))
