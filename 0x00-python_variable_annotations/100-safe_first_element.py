#!/usr/bin/env python3
"""Contain a function to return the first index of an iterable"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ The types of the elements of the input are not know"""
    if lst:
        return lst[0]
    else:
        return None
