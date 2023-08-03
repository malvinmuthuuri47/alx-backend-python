#!/usr/bin/env python3
""" Let's duck type an iterable object """
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Parameters:
            lst: A sequence of iterables

        Return value:
            A list of tuple(s) containing a sequence and an int
    """
    return [(i, len(i)) for i in lst]
