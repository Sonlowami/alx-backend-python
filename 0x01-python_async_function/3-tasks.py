#!/usr/bin/env python3
"""This script contain a usual function that returns a coroutine"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create an asybchronous task and return it"""
    return asyncio.create_task(wait_random(max_delay))
