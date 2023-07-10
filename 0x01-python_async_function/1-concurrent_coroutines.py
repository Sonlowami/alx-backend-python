#!/usr/bin/env python3
"""Executing multiple co-routines at the same time using async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the delay times"""

    results: List(float) = []
    tasks: List(asyncio.Task)

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        result: float = await task
        results.append(result)
    return results
