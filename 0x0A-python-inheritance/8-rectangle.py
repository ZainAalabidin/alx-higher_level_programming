#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""Define module with rectange class"""


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """ "Initilized rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
