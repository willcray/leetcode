"""
https://leetcode.com/problems/longest-consecutive-sequence/
time: O(N)
space: O(N)
Author: Will Cray
Date: 2/24/2022
"""

class Solution:
    
    # input: unsorted list of ints
    # list can be empty
    # reasonable number of ints to be stored on one machine's memory
    # output: int count of longest consecutive sequence
    
    # constraints: O(N) runtime
    
    # ex: [3, 2, 7, 1] -> 3
    # ex: [1, 2, 2, 3] -> 3
    # ex: [] -> 0
    # ex: [9] -> 1
    # ex: [-2, -1, -1, -1, -1] -> 1
    # ex: [1, 2, 3, 31, 34, 33, 32, 31] -> 4
    
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # could sort, but that's Nlog(N)
    
        # time: O(N)
        # space: O(N)
        
        # hash entire list, overwriting input to save space
        nums = set(nums)
        longest = 0
        
        # iterate nums
        for num in nums:
            # only start counting from lowest number in sequence to simplify code 
            if num - 1 not in nums:
                
                count = 1
                # loop until next num doesn't exist, adding to count
                while num + count in nums:
                    count += 1
                        
                longest = max(longest, count)
        
        return longest
                
                
                
                