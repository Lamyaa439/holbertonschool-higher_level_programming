#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
my_list: is the initial list
search: is the element to replace in the list
replace: is the new element
    """
    new_list = []
    for i in my_list:
        if my_list[i] == search:
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]
    return new_list

