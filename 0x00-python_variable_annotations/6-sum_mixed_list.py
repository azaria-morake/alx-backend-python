#!/usr/bin/env python3

from typing import List, Tuple

""" Func: sum_mixed_list() takes a mixture of ints and floats as list 'mxd_lst'
          and it returns their float sum.
"""
def sum_mixed_list(mxd_lst: Tuple[int, float]) -> List[float]:
    return sum(mxd_lst) # naturally returns a float
