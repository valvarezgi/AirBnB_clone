#!/usr/bin/python3
"""Test File_storage
"""

import unittest
import pep8
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Class to test FileStorage"""

    def test_pep8_conformance_FileStorage(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def setUp(self):
        """Set variables"""
        self.my_model = BaseModel()
        self.storaged = FileStorage()

    def test_file_storage_methods(self):
        """test if the methods exist"""
        self.assertTrue(hasattr(self.storaged, "all"))
        self.assertTrue(hasattr(self.storaged, "new"))
        self.assertTrue(hasattr(self.storaged, "save"))
        self.assertTrue(hasattr(self.storaged, "reload"))
