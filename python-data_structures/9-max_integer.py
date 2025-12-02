#!/usr/bin/python3
def max_integer(my_list=[]):
    max_ = 0
    if my_list == []:
        return None
    else:
        for i in range(len(my_list)):
            if max_  > my_list[i]:
                continue
            else: 
                max_ = my_list[1]
    return max_
