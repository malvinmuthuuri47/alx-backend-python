#!/usr/bin/env python3
"""Tasks"""
import asyncio
from typing import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    This function takes an integer and returns a asyncio.Task
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
