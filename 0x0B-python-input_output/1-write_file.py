#!/usr/bin/python3
"""Defines write a file"""


def write_file(filename="", text=""):
    """Write a strint to file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
