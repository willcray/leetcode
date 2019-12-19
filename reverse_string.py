"""
https://leetcode.com/problems/reverse-string/
time: O(N)
space: O(1)
Author: Will Cray
Date: 12/19/2019
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s.reverse()

        """
        for i in range(len(s)):
            if (len(s) - i - 1) > i:
                copy = s[i]
                s[i] = s[len(s) - i - 1]
                s[len(s) - i - 1] = copy
            else:
                break

        """
