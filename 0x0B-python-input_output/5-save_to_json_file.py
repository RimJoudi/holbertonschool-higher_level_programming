#!/usr/bin/python3
""" save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representatio
    """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
