#!/usr/bin/env python

"""
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

n = 0
while True:
    n += 20
    is_dividable = True
    for i in range(1, 21):
        if n % i != 0:
            is_dividable = False
            break
        
    if is_dividable:
        break

print(n)