"""
https://leetcode.com/problems/contains-duplicate/
time: O(N)
space: O(N)
Author: Will Cray
Date: 1/17/2020
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
