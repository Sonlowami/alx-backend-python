#!/usr/bin/python3
"""Define a function to return combined sum of given ints and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return a combined sum of floats and ints as a float"""
    total: float = 0.0
    for num in mxd_lst:
        total += num
    return total
