#!/usr/bin/env python3
"""Conatain a function that returns a callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a callable"""

    def inner_multiplier(num: float) -> float:
        """Return a product of two ints"""
        return num * multiplier

    return inner_multiplier
