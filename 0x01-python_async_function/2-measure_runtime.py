#!/usr/bin/env python3
"""This module contain a function that computes the average time one
random asynchronous operation take to end"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, delay_time: int) -> float:
    """Count how much on average is an async function taking"""

    initial_time: float = time.perf_counter()
    asyncio.run(wait_n(n, delay_time))
    final_time: float = time.perf_counter() - initial_time
    return final_time / n
