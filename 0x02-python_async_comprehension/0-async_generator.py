#!/usr/bin/env python3
"""
Contain an asynchronous generator that takes no argument and yield a random
number between 0 and 10
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """asynchronously wait for 1 minute and yield a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
