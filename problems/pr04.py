#!/usr/bin/env python

"""
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    return str(num) == str(num)[::-1]

digits = [int(f'{i}{j}{k}') for i in range(1, 10) for j in range(10) for k in range(10)]

print(max([i * j for i in digits for j in digits if is_palindrome(i * j)]))