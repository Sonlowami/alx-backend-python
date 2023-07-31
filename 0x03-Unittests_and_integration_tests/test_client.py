#!/usr/bin/env python3
"""Test the GitHubClient"""
from parameterized import parameterized
from typing import Mapping, List
import unittest
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Contain testcases to test the GithubOrgClient class"""

    @parameterized.expand([
        ('google', {'name': 'google'}),
        ('abc', {'name': 'abc'})
        ])
    @patch('client.get_json')
    def test_org(self, name: str, expected: Mapping, jsonmock: Mock) -> None:
        """Test if org works like expected"""

        client: GithubOrgClient = GithubOrgClient(name)
        res: Mock = jsonmock.return_value
        res.return_value = expected
        self.assertEqual(client.org(), expected)
        jsonmock.assert_called_once()

    @parameterized.expand([
        ('google', {'repos_url': 'https://api.github.com/orgs/google/repos'}),
        ('abc', {'repos_url': 'https://api.github.com/orgs/abc/repos'})
        ])
    def test_public_repos_url(self, name: str, expected: Mapping) -> None:
        """Test if a public repo url is returned"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mockorg:
            client: GithubOrgClient = GithubOrgClient(name)
            mockorg.return_value = expected
            self.assertEqual(client.org, expected)
            mockorg.assert_called_once()
            self.assertEqual(client._public_repos_url, expected['repos_url'])

    @parameterized.expand([
        ('google', {'repo_url': 'https://api.github.com/orgs/google/repos'}),
        ('abc', {'repos_url': 'https://api.github.com/orgs/abc/repos'})
        ])
    @patch('client.get_json')
    def test_public_repos(self, name: str,
                          repo: Mapping, mockjson: Mock) -> None:
        """Test if public_repos can return a list of public repositories"""
        payload: Mapping = [
                {'id': 1, 'name': 'google'},
                {'id': 2, 'name': 'atlassian'},
                {'id': 7, 'name': 'microsoft'}
                ]
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mk:
            client: GithubOrgClient = GithubOrgClient(name)
            mk.return_value = repo
            mockjson.return_value = payload
            res: List = client.public_repos()
            self.assertEqual(res, ['google', 'atlassian', 'microsoft'])
            mockjson.assert_called_once()
            mk.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_licence(self, repo, license_key, expected):
        """Test if has_licence returns true if the repo has a license
        or false otherwise"""
        client: GithubOrgClient = GithubOrgClient('google')
        self.assertEqual(client.has_license(repo, license_key), expected)
