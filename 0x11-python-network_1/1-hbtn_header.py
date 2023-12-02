#!/usr/bin/python3
"""  takes in a URL, sends a request and displays the value"""


import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print('{}'.format(response.info().get('X-Request-Id')))
