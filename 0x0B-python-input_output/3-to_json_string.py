#!/usr/bin/python3
""" to_json_string module """
import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object
    Args:
        my_object(string): object to convert
    Returns:
        JSON representation of an object
        """
    return json.dumps(my_obj)
