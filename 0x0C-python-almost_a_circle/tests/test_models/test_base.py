#!/usr/bin/python3
"""test"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test"""
    def test1(self):
        """test 1"""
        b = Base(48)
        self.assertEqual(b.id, 48)

    def test2(self):
        """test 2"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test3(self):
        """test 3"""
        b = Base("Holberton")
        self.assertEqual(b.id, "Holberton")

    def test4(self):
        """test 4"""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test6(self):
        """test 5"""
        self.assertTrue(len(Base.__doc__) > 0)