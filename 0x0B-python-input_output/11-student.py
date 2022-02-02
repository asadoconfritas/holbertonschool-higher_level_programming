#!/usr/bin/python3
"""mod doc"""


class Student:
    """student doc"""
    def __init__(self, first_name, last_name, age):
        """init doc"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""
        if type(attrs) == list:
            dic = {}
            for a, b in self.__dict__.items():
                if a in attrs:
                    dic[a] = b
            return dict(dic)
        else:
            return dict(self.__dict__)

    def reload_from_json(self, json):
        """reload"""
        for a, b in json.items():
            self.__dict__[a] = b
