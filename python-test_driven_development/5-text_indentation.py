#!/usr/bin/python3
"""
Module 5-text_indentation
Defines a function that prints text with specific indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0  # 0 = Start of line (skip spaces), 1 = Inside line (print)

    for c in text:
        if flag == 0:
            if c == ' ':
                continue
            else:
                flag = 1

        if flag == 1:
            if c == '?' or c == '.' or c == ':':
                print(c)
                print()
                flag = 0
            else:
                print(c, end="")
