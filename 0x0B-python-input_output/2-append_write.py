#!/usr/bin/python3
"""define a append a file"""


def append_write(filename="", text=""):
    """how to append a file at end"""
    with open(filename, "a", encoding="utf-8") as f:
	return f.append(text)
