#!/usr/bin/python3
def best_score(a_dictionary):
    out = None
    if a_dictionary and a_dictionary != {}:
        out = max(a_dictionary, key=a_dictionary.get)
    return out
