#!/usr/bin/python3
"""defines how to append file"""


def append_write(filename="", text=""):
    """append text at the end of file."""
    with open(filename, "a", encoding="utf-8") as f:
	return f.write(text)
