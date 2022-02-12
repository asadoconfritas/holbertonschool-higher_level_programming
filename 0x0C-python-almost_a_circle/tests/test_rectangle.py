#!/usr/bin/python3
"""tests rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test rectangle"""
    def testinit(self):
        """test init"""
        a = Rectangle(2, 3, 0, 0, 1)
        self.assertEqual(a.width, 2)
        self.assertEqual(a.height, 3)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 1)

    def testtype(self):
        """test type"""
        self.assertRaises(TypeError, Rectangle, 12, 4.5)
        self.assertRaises(TypeError, Rectangle, 12, [1, 2])
        self.assertRaises(TypeError, Rectangle, 12, 2, 2, (3, 5))
        self.assertRaises(TypeError, Rectangle, 12, 2, 'a', 4)

    def testvalue(self):
        """test value"""
        self.assertRaises(ValueError, Rectangle, 0, 5)
        self.assertRaises(ValueError, Rectangle, 5, -3)
        self.assertRaises(ValueError, Rectangle, 3, 5, -2, 7)
        self.assertRaises(ValueError, Rectangle, 3, 0, 2, 4)

    def testarea(self):
        """test area"""
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """test str"""
        r1 = (2, 4, 1, 1, 16)
        self.assertEqual(str(r1), "[Rectangle] (16) 1/1 - 2/4")
