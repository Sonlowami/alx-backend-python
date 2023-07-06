#!/usr/bin/env python3
"""This module contain a function that returns a list of tuples"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples representing sequences and their lengths"""
    return [(i, len(i)) for i in lst]
