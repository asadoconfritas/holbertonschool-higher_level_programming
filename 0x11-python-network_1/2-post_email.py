#!/usr/bin/python3
"""sends a POST request and displays the body of the response"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
