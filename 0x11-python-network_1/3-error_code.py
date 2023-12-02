#!/usr/bin/python3
""" takes in a URL, sends a request and displays error """


import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
             html = response.read()
             print("{}".format(html.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
