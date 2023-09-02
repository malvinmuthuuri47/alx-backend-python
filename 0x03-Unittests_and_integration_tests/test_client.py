#!/usr/bin/env python3
"""Module documentation"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGitHubOrgClient(unittest.TestCase):
    """Class that implements tests to test the GithubOrgClient module"""
    @parameterized.expand([
        ("google",),
        ("abc",),
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Tests the org function"""
        mock_get_json.return_value = {
                "name": org_name, "description": "Test org"
                }
        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
                client.ORG_URL.format(org=org_name)
                )
        self.assertEqual(
                result, {"name": org_name, "description": "Test org"}
                )
