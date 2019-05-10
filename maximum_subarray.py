"""
https://leetcode.com/problems/maximum-subarray/
Author: Will Cray
Date: 5/10/2019
Time: O(N)
Space: O(1)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # assume that input array has at least one integer
        # assuming a subarray can be the entire array
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, 1
        total_max, curr_max = nums[l], nums[l]
        
        while r < len(nums):
            if curr_max < 0 and nums[r] > curr_max:
                l = r
                curr_max = nums[r]
            else:
                curr_max += nums[r]
            total_max = max(total_max, curr_max)
            r += 1
        
        return total_max