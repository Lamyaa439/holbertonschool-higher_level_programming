#!/usr/bin/python3
"""
Modul of Student to JSON with filter
"""


class Student:
    """Defines a student by first name, last name, and age with filtering."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for k in attrs:
                if k in self.__dict__:
                    res[k] = self.__dict__[k]
            return res
        return self.__dict__
