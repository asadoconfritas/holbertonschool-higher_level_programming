#!/usr/bin/python3
"""unittest for maxint
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def testa(self):
        """testeointenso"""
        self.assertEqual(max_integer([1]), 1)

    def testb(self):
        """testeointenso"""
        self.assertEqual(max_integer([]), None)

    def testc(self):
        """testeointenso"""
        self.assertEqual(max_integer([0, 0]), 0)

    def testd(self):
        """testeointenso"""
        self.assertEqual(max_integer([2.3, 2.7, 3.0, 2.9]), 3.0)

    def teste(self):
        """testeointenso"""
        self.assertEqual(max_integer([1, -2, 3 * 2, -4, 5]), 6)

    def testeo(self):
        """testeointenso"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
