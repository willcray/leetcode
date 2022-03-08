"""
https://leetcode.com/problems/house-robber/
time: O(N)
space: O(1)
Author: Will Cray
Date: 3/8/2022
"""

class Solution:
    
    # input: list of integers
    # input: list has at least one num and few enough to fit in one machine's memory
    # input: values of integers are greater than or equal to zero and small enough to be stored as integers
    
    # output: max sum of money you can steal
    
    # constraint: you can't steal from adjacent homes
    
    # ex. - [1, 2, 3, 1] -> 4
    # ex. - [1] -> 1
    # ex. - [1, 2] -> 2
    # ex. - [0, 2, 1] -> 2
    # ex. - [2, 7, 9, 3, 1] -> 12
    
    def rob(self, nums: List[int]) -> int:
        
        # recursive solution
        # time: O(2^N)
        # space: O(N)
        
        # recursive w/ memoization
        # time: O(N)
        # space: O(N)
        
        # bottom-up DP w/ memo array
        # time: O(N)
        # space: O(N)
        
        """
        num_nums = len(nums)
        
        # handle case of length one
        if num_nums == 1: 
            return nums[0]
        
        # init memo
        memo = num_nums * [0]
        
        # solve case for length one and two
        memo[0], memo[1] = nums[0], max(nums[0], nums[1])
        
        # iterate over nums
        for i in range(2, num_nums):
            
            # can either rob the current house or skip it
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])
        
        # return memo array at last value
        return memo[-1]
        """
        
        # bottom-up DP w/o memo array
        # time: O(N)
        # space: O(1)
        num_nums = len(nums)
        
        # handle case of length one
        if num_nums == 1: 
            return nums[0]
        
        # solve case for length one and two
        prev_prev, prev = nums[0], max(nums[0], nums[1])
        
        # iterate over nums
        for i in range(2, num_nums):
            
            # can either rob the current house or skip it
            curr = max(prev, prev_prev + nums[i])
            
            # update pointers
            prev_prev = prev
            prev = curr
        
        # return memo array at last value
        return prev
        