#!/usr/bin/env python3
"""Unittests and Integration tests"""

import unittest
from parameterized import parameterized, param
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
from typing import List, Union, Mapping, Type, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """
    Encapsulation class that defines test methods for the
    access_nested_map function in utils by providing parameters
    using the parameterized.expand function decorator
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """Tests that the function returns the expected value"""
        self.assertEqual(access_nested_map(nested_map, path), expected_value)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_val):
        """
        This function tests the exception type returned by the
        access_nested_map() and raises fails to pass the test if
        the exception is of an incorrect type
        """
        with self.assertRaises(expected_val) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(type(context.exception), expected_val)
