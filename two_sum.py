"""
https://leetcode.com/problems/two-sum/
Author: Will Cray
Date: 12/13/2018
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # brute force solution is a double nested loop where you try all combinations and return
        # the two indices once you get the sum - time: O(n^2), space: O(1)
        
        # optimal solution uses a hash map/dict
        # time: O(n) because of the sort, space: O(1)
        
        rev_table = {}
        for i in range(len(nums)):
        	num2 = target - nums[i]
            
        	if num2 in rev_table:
        		return [rev_table[num2], i]
        	else:
        		rev_table[nums[i]] = i