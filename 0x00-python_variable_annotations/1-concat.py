#!/usr/bin/env python3
"""This module contain an annotated function to concatenate two strings"""


def concat(str1: str, str2: str) -> str:
    """Concatenate two strings and return the larger string"""
    if isinstance(str1, str) and isinstance(str2, str):
        return str1 + str2
