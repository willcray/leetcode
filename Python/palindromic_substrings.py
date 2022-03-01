"""
https://leetcode.com/problems/palindromic-substrings/
Author: Will Cray
Date: 2/28/2022
Time: O(N^2)
Space: O(1)
"""

class Solution:
    
    # input: string s, of at least one char, up to 1000 chars
    # input: string is lowercase english letters
    
    # output: int count of number of palindromic substrings
    
    # axiom: a single letter is a palindromic substrings
    # axiom: substrings are uniquely identified by indices, rather than the strings themselves
    # i.e. if a substring reoccurs, it's valid
    
    # ex: "dffdd" -> d, f, f, d, d, ff, dd, dffd -> 8
    "dffdd"
    "ffdd"
    "dffd"
    # ex: "r" -> 1
    def countSubstrings(self, s: str) -> int:
        
        """
        # sliding window, checking all substrings
        # increment 
        # time: O(N^3)
        # space: O(1)
        
        total = 0
        
        # use sliding window and increment size of window
        for size in range(1, len(s) + 1):
            
            # slide window
            for start in range(len(s) - size + 1):
                # call palindrome check on substring
                substr = s[start:(start + size)]
                if substr == substr[::-1]: total += 1
        
        return total
        """
    
        
        # DP 
        # store computation of subpalindromes via a matrix for all possible substrings (n x n)
        # time: O(N^2)
        # space: O(N^2)
        
        
        # expand around centers
        # time: O(N^2)
        # space: O(1)
        
        total = 0
        
        for i in range(len(s)):
            
            # handle possible center for odd length palindromes
            total += self.expand(s, i, i)
        
            # possible center for even length (two chars)
            total += self.expand(s, i, i + 1)
        
        return total
        
        
    def expand(self, s: str, low: int, hi: int) -> int:
        
        total = 0
        
        # count number of palindromes 
        while (low >= 0 and hi < len(s)):
            
            if s[low] != s[hi]: 
                break
                
            total += 1
            low -= 1
            hi += 1
        
        return total
        
        