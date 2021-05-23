#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestMaxInteger class
    """
    def test_max(self):
        """
        function to test max_integer function
        """
        
        # Test1: positive numbers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        
        # Test2: negative number(s)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        
        # Test3: empty list
        self.assertEqual(max_integer([]), None)
        
        # Test4: list of strings
        self.assertEqual(max_integer(["Rym", "Holberton", "School"]), "School")
        
        # Test5: testing with floats
        self.assertEqual(max_integer([0.1, 3.2, 8.3, 5.4]), 8.3)
        self.assertEqual(max_integer([0.1, 2, 3, 2.4]), 3)
        
        # Test6: testing with different types
        list_to_test = [1, "Holbie", "Fun", 4]
        self.assertRaises(TypeError)
        
        # Test6: testing with list of only 1 element
        self.assertEqual(max_integer([100]), 100)
        
        # Test7: testing with integer not in a list
        test = 100
        self.assertRaises(TypeError)
        
        
    if __name__ == '__main__':
        unittest.main()
         