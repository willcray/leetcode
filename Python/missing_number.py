"""
https://leetcode.com/problems/missing-number/
Author: Will Cray
Date: 4/25/2019
Time: O(n)
Space: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # assuming at least one number that one number to be 1
        # assuming you're trying to find the missing contiguous number
        # highest number is len(nums)
        # calculate expected sum - probably a formula to eliminate the iteration
        # n + n-1 + n-2 + ... + n-n
        
        # iterative solution
        # start at len of nums (n), iterate to zero by subtracting 1
        n = len(nums)
        expected_sum = 0
        for i in range(n, 0, -1):
            expected_sum += i
        
        # return differece
        return expected_sum - sum(nums)