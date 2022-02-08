#!/usr/bin/python3
"""
    base.py
    mod
    return: base
"""
import json


class Base:
    """ base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to """
        lst = []
        if list_objs is not None:
            for a in list_objs:
                lst.append(a.to_dictionary())
        st = cls.to_json_string(lst)
        filename = str(cls.__name__) + ".json"
        with open(filename, "w") as f:
            f.write(st)

    @staticmethod
    def from_json_string(json_string):
        """ from json """
        auxlst = []
        if json_string is None:
            return auxlst
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == 'Rectangle':
            rett = cls(1, 1)
        else:
            rett = cls(1)
        rett.update(**dictionary)
        return rett

    @classmethod
    def load_from_file(cls):
        """ load from """
        filern = str(cls.__name__) + ".json"
        try:
            with open(filern, "r") as f:
                li = cls.from_json_strings(f.read())
                rvalue = []
                for a in li:
                    rvalue.append(cls.create(**a))
                return rvalue
        except FileNotFoundError:
            return []
