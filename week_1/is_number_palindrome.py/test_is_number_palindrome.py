"""Tests for is number palindrome function"""

import unittest
from solution_is_number_palindrome import is_number_palindrome

class TestNumberPalindromeChecker(unittest.TestCase):
    """
    Class that holds tests for the is number palindrome
    checker
    """

    def test_is_number_palindrome(self):
        """
        Contains tests that checks if  the function 
        returns True when given a valid palindrome.
        """
        # Test with odd length numbers
        self.assertTrue(is_number_palindrome(121))
        # Test with even length numbers
        self.assertTrue(is_number_palindrome(1221))

    def test_is_not_number_palindrome(self):
        """
        Contains tests that checks if  the function 
        returns False when given an invalid palindrome.
        """
        # Test with odd length numbers
        self.assertFalse(is_number_palindrome(123))
        # Test with even length numbers
        self.assertFalse(is_number_palindrome(1241))

if __name__ == "__main__":
    unittest.main()
