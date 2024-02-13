#!/usr/bin/python3
""" Module class Base """
import json
import os.path


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list to json string"""
        if list_dictionaries == None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save object to file"""
        if list_objs == None:
            return []
        else:
            list_objs = [x.to_dictionary() for x in list_objs]
            filename = cls.__name__ + ".json"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """json string to dictionary"""
        if json_string == None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creat an instance"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins
