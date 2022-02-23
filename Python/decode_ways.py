"""
https://leetcode.com/problems/decode-ways/
Author: Will Cray
Date: 2/23/2022
Time: O(N)
Space: O(1)
"""

class Solution:
    
    # input: 
    # string, s that reps encoded numbers
    # reasonable length, has at least one number
    # input will only contain characters 1-26, up to length 100
    
    # output: integer repping number of ways to decode that string
    
    # constraints:
    # all chars are digits, it could include leading zeros, which can only be used on 10, 20 but not as a leading zero
    # entire string must be mapped
    
    # ex - "123" -> [1 2 3], [12 3], [1 23] -> output: 3
    # ex - "" -> output: 0
    
    
    def numDecodings(self, s: str) -> int:
        
        # recursive backtracking solution
        # base case is one char, return 1
        # recursive case is calling function on one letter being used and one on two letters being use
        # sum outputs of all cases
        # time: O(2^N), can add memo to make this O(N)
        # space: O(N)
        
        # DP approach
        # time: O(N), where N is len(s)
        # space: O(1) w/o memo array and O(N) with it (we'll try to remove it after)
        
        if s[0] == "0":
            return 0
        
        # solve initial problems
        two_back = 1
        one_back = 1
        
        # iterate upwards, summing results
        for i in range(1, len(s)):
            
            current = 0
            # check for valid single digit decode using char at i
            if s[i] != "0":
                # current result is a valid path to get to char at i
                current = one_back
            two_digit = int(s[i - 1: i + 1])
            
            # check for possible two digit decode
            
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current
            
        # return last result in memo    
        return one_back
        