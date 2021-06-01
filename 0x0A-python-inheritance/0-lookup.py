#!/usr/bin/python3
"""
Lookup Module
"""


def lookup(obj):
    """
    a function that returns the list of available \
        attributes and methods of an object
    Args:
        obj: the object
    Returns:
        list of available attributes and methods of an object
    """
    return dir(obj)
