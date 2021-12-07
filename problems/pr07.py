#!/usr/bin/env python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

n = 1
count = 0
while True:
    n += 1
    if is_prime(n):
        count += 1
    
    if count == 10001:
        break

print(n)