#!/usr/bin/python3
"""
8-class_to_json.py modul to Returns the dictionary description for JSON
"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object."""
    return obj.__dict__
