#!/usr/bin/python3
"""This module contain an annotated function to add two floats"""


def add(a: float, b: float) -> float:
    """Add a and b and return a float"""
    if isinstance(a, float) and isinstance(b, float):
        return a + b
