#!/usr/bin/env python3

from typing import Tuple, List, Iterator, Sequence

""" Annotate the below function’s parameters and return values 
with the appropriate types """


def element_length(lst: Sequence) -> Iterator[Tuple[int, int]]:
    return [(i, len(i)) for i in lst]
# def element_length(lst: Tuple[int, float]) -> List[Tuple[int, int]]:
#    return [(i, len(i)) for i in lst]


""" def element_length(lst: Tuple[int, float]) -> Tuple[int, float]:
    return [(i, len(i)) for i in lst]
"""
