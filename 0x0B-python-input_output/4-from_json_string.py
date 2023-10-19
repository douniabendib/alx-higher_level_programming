#!/usr/bin/python3
"""Define a json representation"""
import json


def from_json_string(my_str):
    """return from json represent to string"""
    return json.loads(my_str)
