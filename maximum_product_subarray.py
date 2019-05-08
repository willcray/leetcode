"""
https://leetcode.com/problems/maximum-product-subarray/
Author: Will Cray
Date: 5/8/2019
Time: O(N)
Space: O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        MinTemp = nums[0]
        MaxTemp = nums[0]
        Max = nums[0]
        for i in range(1, len(nums)):
            MinTemp, MaxTemp =  min(nums[i], nums[i] * MaxTemp, nums[i] * MinTemp), max(nums[i], nums[i] * MaxTemp, nums[i] * MinTemp)
            Max = max(Max, MaxTemp)
        return Max
    