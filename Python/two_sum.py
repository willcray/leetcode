"""
https://leetcode.com/problems/two-sum/
Author: Will Cray
Date: 2/17/2022
"""
class Solution(object):
    # constraint: can't use the same element (by index, not value)
    # constraint: exactly one solution
    # constraint: values in nums and target are integers, so they can be negative
    # constraint: 2 <= nums.length <= 104
    
    # assumption: nums has at least two integers that sum to target
    # assumption: nums may not be sorted
    
    # example: [1, 3, 3] target = 6; output = [1, 2]
    
    # Solution
    # time: O(len(nums)) -> O(n)
    # space: O(len(nums)) -> O(n)
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force: double nested loop with two pointers


        # optimal: one pass build out dictionary num -> idx (gives constant lookup)
        nums_lookup = {}
        # iterate list
        for i, num in enumerate(nums):
            # subtract current num from target
            diff = target - num

            # check if difference exists AND that it's unique from num
            if diff in nums_lookup and nums_lookup[diff] != i:
                # assumption: this case will always hit
                return [i, nums_lookup[diff]]
            
            # add to hash map
            nums_lookup[num] = i