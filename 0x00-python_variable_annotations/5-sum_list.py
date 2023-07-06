#!/usr/bin/env python3
"""This module contain a function to return a sum of floats in a list
of them"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return a sum of floats from a list"""
    total: float = 0.00
    for num in input_list:
        total += num
    return total
