#!/usr/bin/env python3
"""Contain test cases for testing utility functions
"""
from parameterized import parameterized
from typing import Mapping, Any, Tuple
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Define test cases for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Tuple, expected: Any) -> None:
        """Test if access_nested_map return the expected"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Tuple) -> None:
        """Test if a keyerror is raised when a key passed in
        path doesnot exist in the nested map"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Define test cases to test get_json utility function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, url: str, expected: Any, mock_get: Mock) -> None:
        """Test if get_json calls mock_get, and returns appropriate
        value"""
        mock_get.return_value.json.return_value = expected
        result: Mapping = get_json(url)
        self.assertEqual(result, expected)
        mock_get.assert_called_with(url)


class TestMemoize(unittest.TestCase):
    """Write test cases to test the memoize utility function"""

    def test_memoize(self):
        """Test if a_property returns same result twice while calling
        a_method only one"""

        class TestClass:
            """Create a sample class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """call a_method"""
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mocked_mtd:
            instance = TestClass()
            v1 = instance.a_property()
            v2 = instance.a_property()
            mocked_mtd.assert_called_once()
            self.assertEqual(v1, v2)
