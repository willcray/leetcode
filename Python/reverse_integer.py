"""
https://leetcode.com/problems/reverse-integer/
Author: Will Cray
Date: 4/26/2019
Time: O(n)
Space: O(1)
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # assume input is between -2**31 and 2**31 - 1
        if x is None:
            return 0
        negative = False
        # if negative, store negative flag, convert to positive
        if x < 0:
            negative = True
            x = abs(x)
        # convert int->str
        s = str(x)
        # reverse str
        s = s[::-1]
        # convert str->int, append negative if flag
        x = int(s)
        if negative:
            x = x * -1
        # check if reverse overflowed
        if x > (2**31 - 1) or x < (-2**31):
            return 0
        # return str
        return x