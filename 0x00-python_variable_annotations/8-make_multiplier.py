#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        A function that takes a float(multiplier) as an argument and
        returns a function that multiplies a float by multiplier

        Parameters:
            multiplier: A float

            Callable[[float], float] :
                This can be called as a function which takes a float
                as an argument and returns a float
    """
    def multiply(x: float) -> float:
        """
            A function that multiplies multiplier by a float(x)

            Parameters:
                x: float

            Returns:
                A float that's the result of multiplying x and multiplier
        """
        return x * multiplier
    return multiply
