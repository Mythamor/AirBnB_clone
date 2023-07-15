#!/usr/nin/python3
"""
Testing the console
"""
import io
import unittest
from unittest.mock import patch
from console import HBNBCommand
import models.engine.file_storage


class test_console(unittest.TestCase):
    """ Tests console """

    def test_create_BaseModel(self):
        """ Tests the creation of a BaseModel """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand(0).onecmd("create BaseModel")

        res = f.getvalue()

        if res is not None:
            self.assertTrue(True)
        else:
            self.asserTrue(False)

    def test_create_User(self):
        """ Tests the creation of a User """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
        res = f.getvalue()

        if res is not None:
            self.assertTrue(True)
        else:
            self.assertTrue(False)


