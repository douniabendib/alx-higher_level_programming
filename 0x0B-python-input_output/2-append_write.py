#!/usr/bin/python3
"""Define a append function"""


def append_write(filename="", text=""):
   """how to append a filename""""
   with open(filename, "a", encoding="utf-8") as f:
       return f.write(text)
