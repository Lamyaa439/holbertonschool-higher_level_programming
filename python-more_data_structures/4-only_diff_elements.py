#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = []
    diff_element = []
    for i in set_1:
        for j in set_2:
            if i == j:
                common.append(j)
    for i in set_1:
        if i in common:
            continue
        else:
            diff_element.append(i)
    for j in set_2:
        if j in common:
            continue
        else:
            diff_element.append(j)
    return diff_element
