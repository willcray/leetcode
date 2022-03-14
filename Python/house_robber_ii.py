"""
https://leetcode.com/problems/house-robber-ii/
time: O(N)
space: O(1)
Author: Will Cray
Date: 3/11/2022
"""

class Solution:
    
    # input: nums is a list of integers, repping money able to steal
    # at least one element
    # each int is zero or greater
    # len(nums) able to fit in one machine's memory
    
    # output: max amount of money you can steal on one night
    
    # constraint: can't steal from adjacent houses
    # first house is adjacent to last
    
    # ex. - [1] -> 1
    # ex. - [2, 3, 2] -> 3
    # ex. - [1, 2, 3, 1] -> 4
    # ex. - [1, 2, 3] -> 3, addresses ciruclarity
    
    def rob(self, nums: List[int]) -> int:
        
        # separate problem into two more easily solved problems that resemble House Robber I
        # solutions to House Robber I are as follows
        
        # recursive solution
        # time: O(2^N)
        # space: O(N)
        
        # recursive w/ memoization
        # time: O(N)
        # space: O(N)
        
        # DP, bottom up
        # time: O(N)
        # space: O(N), w/ memo array
        
        # DP, bottom up
        # time: O(N)
        # space: O(1), eliminating memo array
        
        n = len(nums)
        
        if n == 1: 
            return nums[0]
        
        # choose the greater between the two subproblem results
        return max(self.easy_rob(nums, 0, n-1), self.easy_rob(nums, 1, n))
            
    
    def easy_rob(self, nums: List[int], i: int, j: int) -> int:
        
        # could eliminate current to save memory, but it makes it more readable
        prev_prev, prev, current = 0, 0, 0
        
        for idx in range(i, j):
            current = max(nums[idx] + prev_prev, prev)
            prev_prev = prev
            prev = current
            
        return prev
            
            
        
        
        