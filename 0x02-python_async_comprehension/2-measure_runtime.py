#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    A function that measures the total run time for the async_comprehension()
    which is run in parallel 4 times using the asyncio.gather()
    """
    start_time = time.time()
    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
