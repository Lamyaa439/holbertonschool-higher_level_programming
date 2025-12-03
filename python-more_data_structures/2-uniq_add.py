#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_ = 0
    new_list = []
    for i in my_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    for j in new_list:
        sum_ += j
    return sum_
