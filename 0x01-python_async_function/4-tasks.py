#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        A function that takes two params, n and max_delay and spawns
        wait_random n times with the specified max_delay by passing
        max_delay to the function wait_random implemented in the file
        0-basicm_async_syntax.py
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        if not delays or delay >= delays[-1]:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break

    return delays
