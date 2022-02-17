"""
https://leetcode.com/problems/contains-duplicate/
time: O(N)
space: O(N)
Author: Will Cray
Date: 2/17/2022
"""
class Solution:
    
    # input: list of integers, taking on any integer value
    # input: nums is of length at least one
    # input: not sorted
    # output: False if every element is unique
    # True if ANY number occurs at least twice
    
    # ex - [2, 4, 2] -> True
    # ex - [1, 2] -> False
    # ex - [1] -> False
    # ex - 
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # brute force: double nested loop with two pointers, checking
        # for a value occuring twice, immediately return True if the values
        # at both pointers match
        
        # time: O(n^2), where n is len(nums)
        # space: O(1)
        
        # better solution: create set, check if length is shorter than len(nums)
        # this is a one-liner!
        # time: O(n)
        # space: O(n)
        
        # best solution (for now): single loop using a set, checking if we've seen the
        # value before
        # time: O(n), but better amortized
        # space: O(n)
        
        # create set
        hash_lookup = set()
        
        # iterate over nums
        for num in nums:
            # if num in set then return True or add it to the set
            if num in hash_lookup:
                return True
            else:
                hash_lookup.add(num)
            
        return False
        