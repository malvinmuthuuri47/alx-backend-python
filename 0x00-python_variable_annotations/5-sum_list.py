#!/usr/bin/env python3
"""
    Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Calculate the sum of floats passed in as a list

        Parameters:
            (input_list: List[float]) : List of floats

        Return:
            float: The sum of all the floats contained in
                   the list
    """
    return sum(input_list)
