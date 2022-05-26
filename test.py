"""
Este modulo es para hacer testeo del la funcion palindrome
"""

import unittest
from unittest import TestCase
from palindrome import is_palindrome

class TestingFunction(TestCase):
    
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('somos'), True)
        self.assertEqual(is_palindrome('Ligar es ser agil'), True)
        self.assertEqual(is_palindrome('Hola'), False)


if __name__ == '__main__' : 
    unittest.main()