#!/usr/bin/env python3
"""My First Asynchronous module in python. In this module, we create a
random async operation"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """wait for a random number of seconds between 0 and max_delay"""
    delay: float = random.uniform(0, max_delay)
    return await asyncio.sleep(delay, result=delay)
