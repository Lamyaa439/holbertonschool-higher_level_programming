#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    name = dir(hidden_4)
    len_name = len(name)
    for i in range(len_name):
        n = name[i]
        if n[:2] == "__":
            continue
        else:
            print("{}".format(name[i]))
