"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
Author: Will Cray
Date: 2/28/2022
Time: O(log(N))
Space: O(1)
"""

class Solution:
    
    # input: list of sorted but possible pivoted integers
    # input: target int
    # nums is never empty
    # target is never null
    # values are reasonably sized enough to fit in memory, including length of nums
    
    # output: index of target or -1 if it's not present
    
    # NOTE: distinct values
    
    
    # [1, 2, 3], target = 2 -> 1
    # [1], target = 5 -> -1
    # [1, 3, 2] -> target = 2 -> 2
    
    def search(self, nums: List[int], target: int) -> int:
        
        # linear search
        # time: O(N)
        # space: O(1)
        
        # recursive binary search
        # time: O(log(N))
        # space: O(log(N))
        
        # iterative binary search
        # time: O(log(n))
        # space: O(1)
        
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            
            # divide array in half, one half will be sorted.
            mid = lo + (hi - lo) // 2
            if nums[mid] == target: 
                return mid
            
            # sorted side is first half
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # sorted side is second half
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
                
        return -1
            
        
        
        
        