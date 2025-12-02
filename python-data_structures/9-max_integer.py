#!/usr/bin/python3
def max_integer(my_list=[]):
    max_ = 0
    if my_list == []:
        return None
    else:
        for i in range(len(my_list)):
            for j in range (len(my_list) - 1):
                if my_list[i] > my_list[j]:
                    max_ = my_list[i]
                else: 
                    max_ = my_list[j
