"""Tests for is string palindrome function"""

import unittest
from solution_is_string_palindrome import is_string_palindrome

class TestStringPalindromeChecker(unittest.TestCase):
    """
    Class that holds tests for the is string palindrome
    checker
    """

    def test_is_string_palindrome(self):
        """
        Contains tests that checks if  the function 
        returns True when given a valid palindrome.
        """
        # Test with odd number of chars in string
        self.assertTrue(is_string_palindrome("radar"))
        # Test with even number of chars in string
        self.assertTrue(is_string_palindrome("oddo"))
        # Test with upper and lower case combined
        self.assertTrue(is_string_palindrome("Radar"))
        # Testing with single empty space
        self.assertTrue(is_string_palindrome("r adar"))
        # Testing with multiple empty space
        self.assertTrue(is_string_palindrome("r   adar"))
        # Testing with single punctuations
        self.assertTrue(is_string_palindrome("ra,dar"))
        # Testing with multiple punctuations
        self.assertTrue(is_string_palindrome("ra,dar''',,"))
        # Testing with multiple punctuations and spaces
        self.assertTrue(is_string_palindrome("ra,da  r''',   ,"))

    def test_is_not_string_palindrome(self):
        """
        Contains tests that checks if  the function 
        returns False when given an invalid palindrome.
        """
        # Test with odd number of chars in string
        self.assertFalse(is_string_palindrome("hello"))
        # Test with even number of chars in string
        self.assertFalse(is_string_palindrome("done"))

if __name__ == "__main__":
    unittest.main()
