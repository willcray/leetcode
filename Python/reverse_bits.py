"""
https://leetcode.com/problems/reverse-bits/
Time: O(1)
Space: O(1)
Author: Will Cray
Date: 3/30/2022
"""

class Solution:
    
    # input: unsigned integer
    
    # output: integer whose bit representation is the reverse of n's bit representation
    
    # ex. - 4 (100) -> (001) 1
    # ex. - 6 (110) -> (011) 3
    
    def reverseBits(self, n: int) -> int:
    
        # potential approaches

        # convert integer to binary string, reverse the string, convert to integer, return
        # time: O(1)
        # space: O(1)
        
        output, power = 0, 31
        
        # build integer via addition and shifting
        while n:
            output += (n & 1) << power
            n = n >> 1
            power -= 1
    
        return output
    