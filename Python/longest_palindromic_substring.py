"""
https://leetcode.com/problems/longest-palindromic-substring/
Author: Will Cray
Date: 3/17/2022
Time: O(N^2)
Space: O(1)
"""


class Solution:
    
    # input: string, english letters and digits
    # input: s is at least of length one
    
    # output: longest palindromic substring
    
    # ex. - "bab" -> "bab"
    # ex. - "babcac" -> "bab"
    # ex. - "abc" -> "a"
    # ex. - "a" -> "a"
    # ex - "aaaaaa" -> "aaaaaa"
    # ex - "aaabaab" -> "baab"
    
    def longestPalindrome(self, s: str) -> str:
        
        # solution - brute force
        # try all substrings
        # function to check for palindrome, maintain max string
        # time: O(N^3)
        # space: O(N)
        
        # DP
        # time: O(N^2)
        # space: O(N^2)
        
        # expand from middle
        # time: O(N^2)
        # space: O(1)
        
        # init longest substring
        best_l, best_r = 0, 0
        
        # iterate over string with window of size 1 and of size 2
        for i in range(len(s)):
            
            # call function that returns longest palidrome with that being the start
            # single char pivot
            # r is inclusive
            s_l, s_r = self.getLongest(s, i, i)
            if s_r - s_l > best_r - best_l:
                best_l, best_r = s_l, s_r
                
            # double char pivot
            # ensure not at end of list and two characters match
            if i + 1 < len(s) and s[i] == s[i + 1]:
                d_l, d_r = self.getLongest(s, i, i + 1)
                
                if d_r - d_l > best_r - best_l:
                    best_l, best_r = d_l, d_r
            
        # return longest substring
        return s[best_l:best_r + 1]
        
        
    # returning tuple of longest valid palindrome from starting point
    # r is inclusive
    def getLongest(self, s: str, l: int, r: int) -> Tuple[int, int]:
        
        # if moving outward one step is in bounds and still valid, move outward
        while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
            
            l -= 1
            r += 1
        
        return (l, r)