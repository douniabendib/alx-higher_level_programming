#!/usr/bin/python3
def raise_exception():
    try:
        value = "42" + 10 
    except TypeError as e:
        raise e
