#!/usr/bin/python3
""" Read file Module """


def read_file(filename=""):
    """
    Read file function
    """
    with open(filename, encoding="UTF8") as f:
        print(f.read())
