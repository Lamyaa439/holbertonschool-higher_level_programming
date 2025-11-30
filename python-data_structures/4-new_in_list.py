#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i in my_list:
        new_list.append(i)
    len_newlist = len(new_list) - 1
    for j in range(0, len_newlist):
        if j == idx:
            new_list[j] = element
    return new_list
        

