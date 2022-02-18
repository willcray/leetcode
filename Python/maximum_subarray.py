"""
https://leetcode.com/problems/maximum-subarray/
Author: Will Cray
Date: 2/17/2022
Time: O(N)
Space: O(1)
"""


class Solution:
    
    # input: list of at least one integer
    # output: max sum of contiguous subarray
    
    # ex: [1] -> 1
    # ex: [2, -1, 3] -> 4
    # ex: [4, -10, 2] -> 4
    def maxSubArray(self, nums: List[int]) -> int:
        
        # brute force: nested for loop with two pointers, tracking max sum
        # time: O(n^2), where n len(nums)
        # space: O(1)
        
        # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        #             l
        #                              r
        # max_sum = 6
        # curr_sum = 5
        
        # better solution:
        # time: O(N)
        # space: O(1)
        
        # init max and current sum to first value in the list
        max_sum = curr_sum = nums[0]
        
        # iterate through the list with right pointer
        for r in range(1, len(nums)):
            
            # check if it's better to move the start of subarray
            # by seeing if adding it or starting fresh with it would yield a 
            # higher result
            curr_sum = max(nums[r], curr_sum + nums[r])    
            
            # overwrite max sum if greater than max sum
            max_sum = max(curr_sum, max_sum)
            
        # return max sum
        return max_sum