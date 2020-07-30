"""
https://leetcode.com/problems/longest-common-prefix/
Author: Will Cray
Date: 4/26/2019
Time: O(n^2)
Space: O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # address list of size 0
        if len(strs) < 1:
            return ""
    
        # address list of size 1 case for optimization
        if len(strs) == 1:
            return strs[0]
        
        # define common prefix string
        comm_prefix = ""
        # find smallest string
        min_len = len(min(strs))
        
        # outer loop iterating from 0 to len(smallest string)
        for i in range(min_len):
            # get letter at current index
            curr_letter = strs[0][i]
            # inner loop iterates each string, checking at given index
            for s in strs:
                # if anyone doesn't match, return return string
                if s[i] != curr_letter:
                    return comm_prefix
            # append new letter to return string
            comm_prefix += curr_letter
        
        return comm_prefix