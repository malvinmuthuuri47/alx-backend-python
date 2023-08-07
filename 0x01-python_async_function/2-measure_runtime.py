#!/usr/bin/env python3
"""Measure the runtime of an async function using a regular function"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        This function calculates the running time by subtracting
        the difference in time before and after the async function
        is run and then returns that value
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    avg_time = total_time / n
    return avg_time
