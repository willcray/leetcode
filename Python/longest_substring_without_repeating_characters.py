"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Author: Will Cray
Date: 2/23/2022
Time: O(N)
Space: O(N)
"""


class Solution:
    
    # input: string, s 
    # 0 <= s.length <= 5 * 104
    # s is ASCII
    
    # output: int, representing the longest substring w/o repeating chars
    
    # ex. - "abc" -> 3
    # ex. - "abb" -> 2
    # ex. - "" -> 0
    # ex. - "pwwkew" -> 3
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # brute force solution:
        # nested loop with two pointers, maintain a max substring, maintain list / set of currently used letters
        # continue the outer loop when you encounter the first letter twice
        # time: O(n^2) if a set w/ constant lookup is used, O(n^3) otherwise
        # space: O(N)
        
        # sliding window solution
        # time: O(N)
        # space: O(N)
        
        # init char -> index map for current substring
        substr_map = {}
        
        # init max
        max_len = 0
        
        l = 0
        # loop over s
        for r in range(len(s)):
            
            # if letter at right pointer is in set
            if s[r] in substr_map: 
                # explicitly remove repeated string from current pointers
                l = max(l, substr_map[s[r]] + 1)
                
            # take max of current and max substring
            max_len = max(max_len, r - l + 1)
            substr_map[s[r]] = r
                
        return max_len
        
        
        
        