"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
time: O(N)
space: O(N)
Author: Will Cray
Date: 1/18/2020
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        "gaiekdjg" -> 7
        "" -> 0
        None -> 0
        """

        # start, end pointers
        """
        "a b c a b c b b"
                       s
                       e
        "p w w k e w"
        "a z y b a a c d e f g h" -> 7
                   s
                               e
        """

        sub = set()
        longest = 0
        start = 0
        for letter in s:
            # add to substring if no duplicate
            if letter not in sub:
                sub.add(letter)
            else:
                # iterate start pointer until no dups
                while letter in sub:
                    sub.discard(s[start])
                    start += 1

                sub.add(letter)

            # update longest substring value
            if len(sub) > longest:
                longest = len(sub)

        return longest


