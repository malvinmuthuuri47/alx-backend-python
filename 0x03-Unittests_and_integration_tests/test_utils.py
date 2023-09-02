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
