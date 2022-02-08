#!/usr/bin/python3
"""
    rectangle.py
    mod
    return: base
"""
from models.base import Base


class Rectangle(Base):
    """ rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, width):
        """ w setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x get """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """ y get """
        return self.__y
        
    @y.setter
    def y(self, value):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """ area """
        return self.__width * self.__height

    def display(self):
        """ display """
        print(self.__y * '\n', end="")
        for i in range(self.height):
            display = ""
            display += (self.__x * ' ')
            display += (self.width * '#')
            print(display)

    def __str__(self):
        """ self """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -\
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ upd """
        lrg = len(args)
        if lrg >= 1:
            setattr(self, "id", args[0])
        if lrg >= 2:
            setattr(self, "width", args[1])
        if lrg >= 3:
            setattr(self, "height", args[2])
        if lrg >= 4:
            setattr(self, "x", args[3])
        if lrg >= 5:
            setattr(self, "y", args[4])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ todic """
        attr = ['x', 'y', 'id', 'height', 'width']
        res = {}
        for key in attr:
            res[key] = getattr(self, key)
        return res
