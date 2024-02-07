#!/usr/bin/python3
"""`9-student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialized method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that return dictionary of the class"""
        return self.__dict__

    def to_json(self, attrs=None):
        """Method that return value for specific key"""
        if attrs is not None:
            for i in attrs:
                return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
