"""
https://leetcode.com/problems/binary-search/submissions/
Time: O(log(N))
Space: O(1)
Author: Will Cray
Date: 12/18/2019
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while (l <= r):
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            # target is to the right of m
            elif nums[m] < target:
                l = m + 1
            # target is to the left of m
            else:
                r = m - 1

        # we didn't find the target
        return -1
