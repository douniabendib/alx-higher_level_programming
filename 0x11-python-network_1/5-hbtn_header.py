#!/usr/bin/python3
"""  that takes in a URL, sends a request and displays the value """

import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers.get('X-Request-Id')))
