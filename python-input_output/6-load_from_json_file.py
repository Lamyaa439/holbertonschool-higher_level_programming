#!/usr/bin/python3
"""
6-load_from_json_file modul to Write a function that creates
an Object from a JSON fil
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a JSON fil
    """
    with open(filename, 'r') as f:
        return json.load(f)
