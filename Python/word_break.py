"""
https://leetcode.com/problems/word-break/
Author: Will Cray
Date: 3/9/2022
Time: O(N^3)
Space: O(N)
"""

class Solution:
    # input: s is a string
    # input: s is lowercase english letters
    # s is of length at least one
    # wordDict is valid
    # wordDict, dictionary of strings
    
    # output: boolean, true if word can be segmented into words
    # found in wordDict
    
    # axiom: can use word in wordDict more than once
    # axiom: it can only be one word
    
    # ex - "apple" - wordDict = ["apple"] -> True
    # ex - "catsandog" - wordDict = ["cats", "cat, "dog","an"] -> True
    # ex - "leetcode" - wordDict = ["leetcode", "leet"] -> True
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # solution
        # sliding window w/ recursion
        # time: O(2 ^ N)
        # space: O(N)
        
        # recursion w/ memoization (using @lru_cache)
        # time: O(N ^ 3)
        # space: O(N)
        
        # BFS 
        # time: O(N ^ 3)
        # space: O(N)
        
        # DP
        # time: O(N ^ 3)
        # space: O(N)
        
        # hash word dict
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        
        # store answer for zero length string s
        dp[0] = True

        for i in range(1, len(s) + 1):
            # slide window up to j
            for j in range(i):
                
                # if the answer up to j was a word in wordDict and
                # word from j up to i is also in word set, we 
                # have a correct answer up to this point
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                    
        return dp[len(s)]
        
        