#!/usr/bin/env python

"""
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

n1 = sum([i*i for i in range(101)])

# Gauss formula: n * (n + 1) / 2
n2 = (100 * (101) // 2) * (100 * (101) // 2)

print(n2 - n1)
