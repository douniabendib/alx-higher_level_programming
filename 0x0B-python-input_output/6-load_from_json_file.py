#!/usr/bin/python3
"""Define a function create object from json"""
import json


def load_from_json_file(filename):
    """create object from json"""
    with open(filename) as f:
	return json.loads(f)
