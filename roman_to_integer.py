"""
https://leetcode.com/problems/roman-to-integer/
time: O(N)
space: O(1)
Author: Will Cray
Date: 12/19/2019
"""


class Solution:
    def romanToInt(self, s: str) -> int:

        decimal_val = 0
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                    "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        i = 0
        while(i < len(s)):

            try:
                decimal_val += numerals[s[i] + s[i + 1]]
                i += 1

            except (KeyError, IndexError):
                decimal_val += numerals[s[i]]

            i += 1

        return decimal_val
