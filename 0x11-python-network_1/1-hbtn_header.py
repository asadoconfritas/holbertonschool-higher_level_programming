#!/usr/bin/python3
"""display the value of the X-Request-Id variable found in the header"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    if argv[1] is not None:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.headers.get('X-Request-Id'))
