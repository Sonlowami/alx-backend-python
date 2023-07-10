#!/usr/bin/env python3
"""This module contain a python function to return a sorted list
of floats representing delay times of random asynchronous operations"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The implementation of this function resembles wait_n function
    in 1-concurrent_coroutines. The only difference is that creation of
    a coroutine is outsourced to task_wait_random"""
    results: List(float) = []
    tasks: List(asyncio.Task)

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        result: float = await task
        results.append(result)
    return results
