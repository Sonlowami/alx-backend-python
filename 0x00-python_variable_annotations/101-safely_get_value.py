#!/usr/bin/python3
"""This module contain a function that returns a key from a dictionary"""
from typing import Union, Mapping, Any


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[Any, None] = None) -> Union[Any, None]:
    """Return a key from a dictionary if it is there. Return the default
    otherwise"""
    if key in dct:
        return dct[key]
    else:
        return default
