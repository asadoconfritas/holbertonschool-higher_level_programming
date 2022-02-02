#!/usr/bin/python3
"""mod doc"""
import json


def save_to_json_file(my_obj, filename):
    """save json"""
    with open(filename, 'w+', encoding='utf8') as f:
        return json.dump(my_obj, f)
