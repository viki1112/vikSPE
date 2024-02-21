#!/usr/bin/env python

import math

def root(n):
    if n<0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(n)

def factorial(n):
    if n<0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

def log(n):
    if n<=0:
        raise ValueError("Logarithm is not defined for non-positive numbers.")
    return math.log(n)

def power(base, exponent):
    return math.pow(base,exponent)
