"""
https://leetcode.com/problems/number-of-1-bits/
Time: O(1)
Space: O(1)
Author: Will Cray
Date: 3/30/2022
"""


class Solution:
    
    # input: integer n
    # output: integer for the number of '1' bits in n's binary representation
    
    def hammingWeight(self, n: int) -> int:
    
        # iterate through each bit, modding by 2, counting number of one's
        # time: O(1)
        # space: O(1)
        
        count = 0
        
        # iterate while not zero
        while n:
            # mod to see if least significant bit is one or zero
            # if it's one, add one to count
            if n & 1 == 1: 
                count += 1
            
            # shift n
            n = n >> 1
        
        # return count
        return count
    
        
        # alternative, slightly faster - removing least significant bit that's a one
        # time: O(1)
        # space: O(1)