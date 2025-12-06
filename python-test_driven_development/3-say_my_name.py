#!/usr/bin/python3
"""
Module 3-say_my_name
Defines a function that prints a specific name message.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Check first_name type
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check last_name type
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted string
    print("My name is {} {}".format(first_name, last_name))
