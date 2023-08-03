#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        A function that takes a string(k) and a Union(containing
        an int/float and returns a tuple of str and floats with
        the float squared

        Parameters:
            k: String
            v: A union of int/floats

        Return value:
            A Tuple whose first element is the string(k) and the
            second element is the squared float
    """
    return (k, v ** 2)
