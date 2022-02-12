#!/usr/bin/python3
"""
    square.py
    mod
    return: sq
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square doc """
    def __init__(self, size, x=0, y=0, id=None):
        """ init """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size get """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        setattr(self, "width", size)
        setattr(self, "height", size)

    def __str__(self):
        """ self str """
        str1 = "{}/{}".format(self.x, self.y)
        str2 = self.width
        return "[Square] ({}) {} - {}".format(self.id, str1, str2)

    def update(self, *args, **kwargs):
        """ upd doc """
        lrg = len(args)
        if lrg >= 1:
            setattr(self, "id", args[0])
        if lrg >= 2:
            setattr(self, "size", args[1])
        if lrg >= 3:
            setattr(self, "x", args[2])
        if lrg >= 4:
            setattr(self, "y", args[3])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ to dic """
        my_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return my_dict
