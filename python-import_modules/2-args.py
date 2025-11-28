#!/usr/bin/python3
import sys
arg_list = sys.argv
len_list = len(arg_list)
print("{} argument:".format(len_list - 1))
for i in range(1, len_list):
    print("{}: {}".format(i, arg_list[i]))
