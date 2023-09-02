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


class TestGetJson(unittest.TestCase):
    """This class encapsulates all test methods for the utils.get_json()"""
    @parameterized.expand([
        # Define test data
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        This method simulates a call to an external API and tests
        that the return values are the same as the parameters defined
        in the test_data below.

        The url is the first value in the test_url_payload_pairs list
        and the expected response is the dictionary in the list

        You use the python mock object to simulate the request to the
        external API
        """

        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call function under test
            result = get_json(test_url)

            # Assert the no. of times the mock was called
            mock_get.assert_called_once_with(test_url)

            # Assert that results match expected payload
            self.assertEqual(result, test_payload)
