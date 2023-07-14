#!/usr/bin/env python3
"""Contain an asynchronous function to measure runtime of operations"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure time it takes to run 4 async_comprehension operations"""
    start_time: float = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    final_time: float = time.perf_counter() - start_time
    return final_time
