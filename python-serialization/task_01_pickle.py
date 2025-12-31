#!/usr/bin/env python3
"""
This module named task_01_pickle.py
"""
import pickle


class CustomObject:
    """
    a custom class named CustomObject
    This class have the following attributes:
    name (a string)
    age (an integer)
    is_student (a boolean)
    """
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object attributes in a formatted manner."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance to a file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, PermissionError, pickle.PicklingError) as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads an instance of CustomObject from a file."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, Exception):
            return None
