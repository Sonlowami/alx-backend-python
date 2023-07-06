#!/usr/bin/python3
"""This module contain an annotated function to return a floor of a float"""
import math


def floor(n: float) -> int:
    """Return the floor of a float"""
    if isinstance(n, float):
        return math.floor(n)
