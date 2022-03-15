"""
https://leetcode.com/problems/longest-repeating-character-replacement/
Author: Will Cray
Date: 3/15/2022
Time: O(N)
Space: O(N)
"""

from collections import Counter

class Solution:
    
    # input: string S, consisting of only uppercase english letters
    # input: int k, number of characters we can change
    # s always has at least one letter
    # k >= 0
    # length of S is small enough to fit into one machine's memory
    
    # output: integer length of longest same-letter substring after the transformations
    
    # ex. - "CCB", k = 1 -> 3
    # ex. - "CCB", k = 2 -> 3
    # ex. - "CBCFFDF", k = 1 -> 4
    # ex. - "CBCFFDF", k = 2 -> 5
    
    # AACBDBDB, k = 2
    def characterReplacement(self, s: str, k: int) -> int:
        
        # function for computing longest substring of same letter
        # O(N)
        # space: O(1)
        
        # call above function on every possible combination
        # time: O(N * k)
        # space: O(N * K)
        
        # sliding window
        # time: O(N)
        # space: O(N)
        
        count = Counter()
        
        # max_count is the number of occurences for the most frequently occuring char
        # max_len is the value we're looking for, len of longest same char substring + k subs
        max_len = max_count = 0
        
        for i in range(len(s)):
            
            count[s[i]] += 1
            
            max_count = max(count[s[i]], max_count)
            
            # the answer is always max_len + k
            if max_len < max_count + k:
                max_len += 1
            
            # we've used to many substitutes, remove character from start of subsequence/window
            else:
                count[s[i - max_len]] -= 1
        
        return max_len
