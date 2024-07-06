#!/usr/bin/env python3

"""
Write a type-annotated function make_multiplier 
that takes a float 'multiplier' as argument 
and returns a function that multiplies
a float by multiplier.
"""

def make_multiplier(multiplier: float) -> float:
    def x(multiplier):
        return 1.0 * multiplier
    return x


""" def make_multiplier(multiplier: float) -> float:
    def x(multiplier):
        return 1.0 * multiplier
    return x(multiplier)
"""