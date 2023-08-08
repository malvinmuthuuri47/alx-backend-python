#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random


async def async_generator() -> list[float]:
    """
    An async func that takes no arguments, executes a loop 10 times, each
    time asynchronously waits 1 second, then yields a random number between
    0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        i = random.uniform(0, 10)
        yield i
