#!/usr/bin/python3
"""
This  module named task_00_basic_serialization.py with the following functions
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    The function serialize_and_save_to_file take 2 parameters:
    data: A Python Dictionary with data
    filename: The filename of the output JSON file.
    If the output file already exists it should be replaced.
    """
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    The function load_and_deserialize take 1 parameters:
    filename: The filename of the input JSON file This function returns
    a Python Dictionary with the deseialized JSON data from the file.
    """
    with open(filename, "r") as f:
        return json.load(f)
