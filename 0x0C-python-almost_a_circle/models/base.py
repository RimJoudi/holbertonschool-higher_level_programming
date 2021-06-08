#!/usr/bin/python3
""" Base module """
import json


class Base:
    """ Base class """
    __nb_objects = 0  # private class attrib

    def __init__(self, id=None):
        """
        Init method
        Args:
            id(int): given id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        list = []
        if list_objs is None:
            list = []
        else:
            for i in list_objs:
                list.append(cls.to_dictionary(i))
        with open("{}.json".format(cls.__name__), 'w', encoding="UTF8") as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        list = []
        if json_string is None or json_string == "":
            return "[]"
        else:
            return json.loads(json_string)
