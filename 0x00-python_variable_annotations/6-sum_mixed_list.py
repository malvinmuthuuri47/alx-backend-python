#!/usr/bin/env python3
""" Complex types - mixed list module """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Add a list of integers and floats and return the sum

        Parameters:
            mxd_lst: A list of int and floats

        Return Value:
            A total float addition of all the elements in the list
    """
    return sum(mxd_lst)
