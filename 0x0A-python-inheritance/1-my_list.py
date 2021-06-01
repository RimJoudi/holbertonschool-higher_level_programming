#!/usr/bin/python3
"""
MyList module
"""


class MyList(list):
    """
    MyList class that inherits from List
    """
    def print_sorted(self):
        """
        prints a sorted list
        """
        print(sorted(self))
