"""
https://leetcode.com/problems/3sum
Author: Will Cray
Date: 2/23/2022
Time: O(N^2)
Space: O(N)
"""


class Solution:
    
    # input: list of ints
    # output: list of UNIQUE triplets, which are lists of three UNIQUE integers
    
    # constraints: 
    # return empty list when no triplets exist
    # all triplets are unique, irrespective of order
    # each triplet contains only unique numbers that sum to zero
    
    # ex. - [1, 2] -> []
    # ex. - [1, -1, 0] -> [[1, -1, 0]]
    # ex. - [1, -1, 0, -1, 1] -> [[1, -1, 0]]
    # ex. - [2, -1, -1] -> []
    
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # brute force solution
        # triple nested loop
        # add triplets to a set to remove dups
        # return set
        # time: O(N^3), where N == len(nums)
        # space: O(N), for the set
        
        # better solution: sort first and use two pointers
        # time: O(N^2)
        # space: O(N)
        
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            # remaining values can't sum to zero
            if num > 0: break
            
            # if current num isn't the same as the previous num
            if i == 0 or num != nums[i-1]: self.twoSumII(nums, i, res)
                
        return res
            

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        # while lower num is smaller than higher num
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            # found a triplet
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                # ensure at least one of the three numbers is unique moving forward
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                
            
        
        # extract one number, treat the rest as a two sum problem, don't sort the list but use hash instead
        # time: O(N^2)
        # space: O(N)
        
            