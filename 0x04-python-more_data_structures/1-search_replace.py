#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newst = my_list[:]
    for i, a in enumerate(newst):
        if a == search:
            newst[i] = replace
    return newst
