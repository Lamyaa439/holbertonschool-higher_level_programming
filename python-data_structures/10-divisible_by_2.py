#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    to_list = 0
    for i in my_list:
        if i % 2 == 0:
            to_list = True
        else:
            to_list = False
        new_list.append(to_list)
    return new_list 
