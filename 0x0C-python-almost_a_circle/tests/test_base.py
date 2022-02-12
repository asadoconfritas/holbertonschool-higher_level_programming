#!/usr/bin/python3
""" base doc """
import unittest
from models.base import Base
import json
import pycodestyle
from os import path


class TestCodeFormat(unittest.TestCase):
    """Test Code Format doc"""
    def test_pycodestyle_conformance(self):
        """test pepocho doc"""
        pepocho = pycodestyle.StyleGuide(quiet=True)
        res = pepocho.check_files(['../../models/base.py'])
        self.assertEqual(res.total_errors, 1,
                         "Found code style errors (and warnings).")

class TestBase(unittest.TestCase):
    """ test base """
    def testtype(self):
        """type check"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        c = Base(98)
        self.assertEqual(c.id, 98)
        d = Base(-1)
        self.assertEqual(d.id, -4)
