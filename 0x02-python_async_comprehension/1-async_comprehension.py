#!/usr/bin/env python3
"""Contain a co-routine to read from async generator using
comprehension"""
from typing import Sequence
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Sequence[float]:
    """Call async generator and return the result"""
    result: Sequence[float] = [item async for item in async_generator()]
    return result
