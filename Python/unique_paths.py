"""
https://leetcode.com/problems/unique-paths/
Author: Will Cray
Date: 3/9/2022
Time: O(M * N)
Space: O(M * N)
"""

from math import factorial

class Solution:
    
    # input: m x n grid via two integers
    # input: m and n are at least 1
    
    # output: number of UNIQUE ways to get to m - 1, n - 1
    
    # constrainsts: robot can only move down or right at each point
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        # recursive approach
        # time: 2 ^ (max(n, m))
        # space: O(N * M)
        # return 1 if robot is at m - 1, n - 1
        # recursive call on all valid moves from current location, adding them together
        # return total
        
        # recursive w/ memoization of robot at a current location
        # time: O(N * M)
        # space: O(N * M)
        
        # DP, bottom up approach, w/ memo
        # time: O(N * M)
        # space: O(N * M)
        
        # init memo
        memo = m * [n * [1]]
        
        # iterate entire grid, filling in answer
        for i in range(1, m):
            for j in range(1, n):
                
                # value at i, j = the sum of the answer for the two valid moves
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
                
        
        return memo[-1][-1]
    
    
        # Leveraging binomial coefficients for one-liner w/ better efficiency
        # time: O((M + N)(log(M + N)loglog(M + N))^2) -- python's factorial implementation
        # space: O(1)
        """
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
        """
    
        
        