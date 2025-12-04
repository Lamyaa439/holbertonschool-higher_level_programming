#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_element = []
    for i in set_1:
        for j in set_2:
            if i == j:
                continue
            else:
                diff_element.append(j)
                diff_element.append(i)
    return diff_element
