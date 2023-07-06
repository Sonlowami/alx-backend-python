#!/usr/bin/env python3
"""This module contain a function that returns a key from a dictionary"""
from typing import Union, Mapping, TypeVar

T = TypeVar['T']


def safely_get_value(dct: Mapping[T, T], key: T,
                     default: Union[Any, None] = None) -> T:
    """Return a key from a dictionary if it is there. Return the default
    otherwise"""
    if key in dct:
        return dct[key]
    else:
        return default
