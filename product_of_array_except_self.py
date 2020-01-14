"""
https://leetcode.com/problems/product-of-array-except-self/
time: O(N)
space: O(N)
Author: Will Cray
Date: 1/13/2020
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [1, 1, 2, 6]
        # [24, 12, 4, 1]

        output = [1] * len(nums)
        left_side = [1] * len(nums)
        right_side = [1] * len(nums)

        p1 = 1
        p2 = 1

        # get left side values
        for i in range(len(nums)):
            left_side[i] *= p1
            p1 *= nums[i]

            right_side[len(nums) - 1 - i] *= p2
            p2 *= nums[len(nums) - 1 - i]

        # fill output array
        for i in range(len(nums)):
            output[i] = left_side[i] * right_side[i]

        return output


