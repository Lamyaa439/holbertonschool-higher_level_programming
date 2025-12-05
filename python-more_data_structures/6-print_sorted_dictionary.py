#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_item = []
    for item in a_dictionary.items():
        list_item.append(item)
    list_item.sort()
    for key, value in list_item:
        print("{}: {}".format(key, value))
