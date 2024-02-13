#!/usr/bin/python3
""" Module that contains class Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str speceial method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """update method"""
        if len(args) > 0:
            self.id = args[0] if len(args) > 0 else self.id
            self.__size = args[1] if len(args) > 1 else self.__size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.x
        else:
            if len(kwargs) > 0:
                for key, val in kwargs.items():
                    self.id = val if key == "id" else self.id
                    self.__size = val if key == "size" else self.__size
                    self.x = val if key == "x" else self.x
                    self.y = val if key == "y" else self.y

    def to_dictionary(self):
        """dictionary method with properaty"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
