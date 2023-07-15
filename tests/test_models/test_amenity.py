#!/usr/bin/python3
"""
Tests for class Amenity
"""


import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """
    Tests for class Amenity
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes models to test
        """
        super().__init__(*args, **kwargs)
        self.test_class = Amenity
        self.test_name = "Amenity"


if __name__ == "__main__":
    unittest.main()
