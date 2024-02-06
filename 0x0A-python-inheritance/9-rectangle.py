#!/usr/bin/python3
"""Define module with rectange class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """ "Initilized rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
