"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
time: O(log(N))
space: O(1)
Author: Will Cray
Date: 3/11/2022
"""

class Solution:
    
    # input: nums list of UNIQUE ints, that's sorted but rotated up to len(nums) times
    # input: nums has at least one element, small enough to fit in one machine's memory
    
    # output: min element of array
    
    # constraint: O(log(N)) runtime
    
    # ex. - [3, 1, 2], rotated once -> 1
    # ex. - [2, 3, 1], rotated twice -> 1
    # ex. - [1, 2, 3], rotated n times -> 1
    # ex. - [9] -> 9
    # ex. [3, 4, 5, 1, 2] -> 1
    # ex. - [17, 11, 13, 15] -> 11
    
    def findMin(self, nums: List[int]) -> int:
        
        # approach: continually divide problem in half
        
        # recursively:
        # time: O(log(N))
        # space: O(log(N))
        
        # iteratively:
        # time: O(log(N))
        # space: O(1)
        
        # look at first and last element
        first, last = 0, len(nums) - 1
        
        # search while 
        while first < last:
            
            mid = first + (last - first) // 2
            
            # we know pivot must be to the right of the middle
            if nums[mid] > nums[last]:
                first = mid + 1
            
            # pivot is to the left of the middle
            else:
                last = mid
            
        return nums[first]
            
            
            