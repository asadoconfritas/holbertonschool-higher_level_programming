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

	def test_documentation(self):
       		"""documentation"""
	        self.assertTrue(len(Base.__doc__) > 0)

	def test_class_doc(self):
        	"""documentation"""
		self.assertTrue(len(Base.__doc__) > 0)

    	def test_json_string_doc(self):
        	"""documentation"""
        	self.assertTrue(len(Base.to_json_string.__doc__) > 0)

    	def test_save_file(self):
        	"""documentation"""
        	self.assertTrue(len(Base.save_to_file.__doc__) > 0)

    	def test_from_json(self):
        	"""documentation"""
        	self.assertTrue(len(Base.from_json_string.__doc__) > 0)

    	def test_create(self):
        	"""documentation"""
        	self.assertTrue(len(Base.create.__doc__) > 0)

    	def test_load_file(self):
        """documentation"""
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)
