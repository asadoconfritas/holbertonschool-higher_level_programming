#!/usr/bin/python3
def uniq_add(my_list=[]):
    items = []
    cuenta = 0
    for i in my_list:
        if i not in items:
            items.append(i)
            cuenta += i
    return cuenta
