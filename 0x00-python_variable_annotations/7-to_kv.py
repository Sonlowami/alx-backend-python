#!/usr/bin/env python3
"""Contain a string that returns a tuple of a string ant int or float"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple"""
    return (k, v*v)
