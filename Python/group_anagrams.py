"""
https://leetcode.com/problems/group-anagrams/
Author: Will Cray
Date: 2/24/2022
Time: O(N * M)
Space: O(N * M)
"""

from collections import defaultdict

class Solution:
    # input: list of strings, strs
    # all lower case, english letters
    # at least one element in the input
    # each string is at least length one
    
    # output: List of list of strings, the groups of anagrams
    
    # ex. - ["tea", "ate", "pea", "sea", "note", "tone"] -> [["tea", "ate"], ["pea"], ["sea"], ["note", "tone"]]
    # ex. - [""] -> [[""]]
    
    # assumption: anagrams can be returned in any order
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # initial idea: 
        # nested loop through each string, checking if each is an anagram
        # use set or dictionary to determine if one string is an anagram of another string
        # if you don't use a set / dictionary, you can iterate and look for each character, which amkes it O(n^3 * M)
        # time: O(N^2 * M), where N is num of strings, M is the length of the longest string
        # space: O(N * M)
        
        # better solution: could sort each string, and the list, keeping a map to unsorted strings, compare directly
        # time: O(N * M log(M))
        # space: O(N * M)
        
        # improved: use count dictionary
        # time: O(N * M)
        # space: O(N * M)
        
        # create map for that maps character count array -> groups of anagrams
        # we'll return the values of this map
        groups = defaultdict(list)
        
        for s in strs:
            # only using lower-case, English letters
            count = 26 * [0]
            for c in s:
                # ord() returns unicode encoding of a char
                # encoding is relative to the start of lexicon, 'a'
                count[ord(c) - ord('a')] += 1
            
            # append current string to whichever group has same character count
            groups[str(count)] += [s]
        
        return groups.values()
        
        
        