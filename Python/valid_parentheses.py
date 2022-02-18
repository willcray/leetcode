"""
https://leetcode.com/problems/valid-parentheses/
time: O(N)
space: O(N)
Author: Will Cray
Date: 2/18/2022
"""

class Solution:
    # input: two strings, s and t
    # input: s and t are at least length one
    
    # output: boolean, true if t is an anagram of s, false otherwise 
    
    # assuming that there can't be superfluous letters in t to be a valid
    # anagram
    
    # ex - s: "go", t: "ogo" -> false
    # ex - s: "tall", t: "mall" -> false
    # ex - s: "seek", t: "kese" -> true
    def isAnagram(self, s: str, t: str) -> bool:
        
        # better solution: sorting both strings, returning false true if equal
        # false otherwise
        # time: O(nlog(n)), n len(s)
        # space: O(1)
        
        # even better solution: 
        # time: O(n)
        # space: O(1)
        
        if len(s) != len(t): return False
        
        # create hash map that maps char -> occurences
        # increment each time a char in s has an occurence
        # decrement each time a char in t has an occurence
        # all counts at the end should be zero
        char_map = {}
        for i in range(len(s)):
            if s[i] not in char_map: 
                char_map[s[i]] = 1
            else:
                char_map[s[i]] += 1
                
            if t[i] not in char_map: 
                char_map[t[i]] = -1
            else:
                char_map[t[i]] -= 1
        
        # loop through the map and ensure all values are zero
        for count in char_map.values():
            if count != 0: return False
            
        return True
        
        