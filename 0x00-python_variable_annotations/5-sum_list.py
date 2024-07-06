#!/usr/bin/env python3

from typing import List, Iterator
"""
Func = sum_list(): takes a list of floats 'input_list', returns their float sum.

sum_list() ::= 'def' identifier'():' 
"""

def sum_list(input_list: List[float]) -> List[float]:
    return sum(input_list)