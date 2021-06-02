#!/usr/bin/python3
""" Read file Module """


def read_file(filename=""):
    """
    Read file function
    Args:
        filename(string): the given file name
    """
    with open(filename, 'r', encoding="UTF8") as f:
        print(f.read(), end="")
