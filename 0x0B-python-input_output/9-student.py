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
