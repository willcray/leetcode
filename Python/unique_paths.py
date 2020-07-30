"""
https://leetcode.com/problems/unique-paths/
time: O(N*M)
space: O(N*M)
Author: Will Cray
Date: 1/14/2020
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # solution 1 - DFS with a break condition of returning 1, sum all calls

        # solution 2 - dynamic programming

        # init memo array
        memo = [[1] * m for i in range(n)]

        # fill memo array
        for i in range(1, n):
            for j in range(1, m):

                # recurrence condition
                memo[i][j] = memo[i][j - 1] + memo[i - 1][j]

        return memo[-1][-1]
