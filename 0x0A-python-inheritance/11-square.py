#!/usr/bin/python3
"""Import `9-rectangle` module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initilized Square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns area of rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """Returns a string"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
