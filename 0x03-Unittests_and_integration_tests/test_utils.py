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


class TestMemoize(unittest.TestCase):
    """This class encapsulates tests for the utils.memoize function"""
    def test_memoize(self):
        """
        This function tests the return value of the a_method
        and also the number of times it has been called
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        # Patch a_method to track calls
        with patch.object(test_instance, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that a_method was called only once
            mock_a_method.assert_called_once()

            # Assert that results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
