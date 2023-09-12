#!/usr/bin/python3
"""Define a read file."""


def read_file(filename=""):
   """print a content of file"""
   with open(filename, "r", encoding="utf-8") as f:
      read_file = f.read()
      ¬print(read_file, end ="")
