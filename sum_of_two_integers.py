"""
https://leetcode.com/problems/roman-to-integer/
time: O(1)
space: O(1)
Author: Will Cray
Date: 1/6/2020
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:

        # assuming a and b are non-null integer values

        # solution 1:
        # using a for-loop to count from a to b
        # this wouldn't be valid in c++ (uses + operator)
        # so it's probably not what they're looking for

        # solution 2:
        # use logs and log power rules to eliminate addition in equation a + b = c
        # a and b must be positive to convert to a product

        # solution 3:
        # bitwise AND and XOR operations
        MIN = 0x80000000
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if a <= MAX:
            return a
        else:
            return ~(a ^ mask)
