#!/usr/bin/python3
""" MyInt module """


class MyInt(int):
    """
    MyInt class inherited from int
    """
    def __eq__(self, other):
        """
        eq function
        Args:
            other(int): the given value
        Returns:
            the inverted operator !=
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        ne function
        Args:
            other(int): the given value
        Returns:
            the inverted operator ==
        """
        return super().__eq__(other)
