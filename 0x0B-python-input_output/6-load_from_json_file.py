#!/usr/bin/python3
"""mod doc"""
import json


def load_from_json_file(filename):
    """load json"""
    with open(filename) as f:
        return (json.load(f))
