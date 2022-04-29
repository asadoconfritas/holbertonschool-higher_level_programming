#!/usr/bin/python3
"""py script"""
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1] is not None:
        res = requests.get(argv[1])
        print(res.headers.get('X-Request-Id'))
