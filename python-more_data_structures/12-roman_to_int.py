#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    int_ = 0
    to_int = 0
    for i in roman_string:
        int_ = roman_dict[i]
        to_int += int_
    return to_int
