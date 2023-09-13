#!/usr/bin/python3
"""Define function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """write object file using json representation"""
    with open(filename, "w") as f:
	json.dumps(my_obj, f)
