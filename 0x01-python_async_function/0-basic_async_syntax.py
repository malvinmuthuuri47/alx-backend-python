#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        An async method that takes a param representing the max_delay
        and returns the same param after passing it through the random.
        uniform method which is used to perform an await using the
        event loop asyncio.

        Parameters:
            @max_delay: Its the integer that's used as the upper limit
            for the random.uniform method to return a random floating
            point number.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
