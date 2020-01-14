"""
https: // leetcode.com/problems/generate-parentheses/
time: O(?)
space: O(n*2) = O(n)
Author: Will Cray
Date: 1/13/2020
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def placeBrackets(builder, open_left, closed_left):

            # base case - open_left and closed_left are 0
            if open_left == 0 and closed_left == 0:
                # validate it's a valid combination, append to ret_list if it is
                return [builder]

            # determine what brackets we can place

            # if we have an open bracket remaining, place it
            if open_left > 0 and closed_left > open_left:
                return placeBrackets(builder + "(", open_left - 1, closed_left) + placeBrackets(builder + ")", open_left, closed_left - 1)

            # if we have less open brackets remaining than closed brackets, place a closed bracket
            elif closed_left > open_left:
                return placeBrackets(builder + ")", open_left, closed_left - 1)

            else:
                return placeBrackets(builder + "(", open_left - 1, closed_left)

        # n = 1
        # [ () ]

        # n = 2
        """
        [
            "()()",
            "(())"
        ]
        """

        # handle null input
        if n == None:
            return []

        # recursive approach
        return placeBrackets("", n, n)






