#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    for key, value in a_dictionary.items():
        if max_value < value:
            return key
