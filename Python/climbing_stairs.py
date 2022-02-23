"""
https://leetcode.com/problems/climbing-stairs/
Author: Will Cray
Date: 2/23/2022
Time: O(N)
Space: O(1)
"""

class Solution:
    # input: n, an integer 1 <= n <= 45
    # n won't be None
    
    # output: integer, representing the number of permutations to get to the nth stair
    
    # ex. - n = 2, 
    # steps_taken = [1, 1], [2], NO: [1, 2], output: 2
    
    # ex - n = 4 -> [1, 1, 1, 1], [1, 1, 2], [2, 1, 1], [1, 2, 1], [2, 2] -> output: 5
    
    # ex. - n = 5 -> [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2] -> output: 8
    
    # constraints: can't overshoot the top step, can't take zero steps
    def climbStairs(self, n: int) -> int:
        
        # recursive backtracking
        # base case is n = 1, return 1
        # recursive step will sum all results
        # time: O(2^n)
        # space: O(n)
        
        # dp solution / Fibonacci Number
        # iteratively building a solution from bottom up, memoizing results
        # time: O(n)
        # space: O(1), if we eliminate the memo array
        
        # create memo
        # memo = (n + 1) * [0]
        
        # solve base case
        # memo[1] = 1 
        
        # more optimal without memo
        if n == 1 or n == 2: return n
        
        # take iterative step
        prev_prev = 1
        prev = 2
        curr = 3
        
        # loop until we get to n
        for i in range(3, n + 1):
            
            # reference the last two solutions and store current solution
            # memo[i] = memo[prev] + memo[prev_prev]
            
            # without memo
            curr = prev_prev + prev
            prev_prev = prev
            prev = curr
        
        # return solution
        return curr