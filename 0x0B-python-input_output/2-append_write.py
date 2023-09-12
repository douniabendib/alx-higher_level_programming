#!/usr/bin/python3
"""Define a append function"""


def append_write(filename="", text=""):
    """how to append a text at end of file
      
    Arg:
        filename (str): name of file
      	text (str):text append at end

    Return:
	the number of characters added
    """
   with open(filename, "a", encoding="utf-8") as f:
       return f.write(text)
