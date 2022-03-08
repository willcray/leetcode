"""
https://leetcode.com/problems/longest-increasing-subsequence/
time: O(N^2)
space: O(N)
Author: Will Cray
Date: 3/8/2022
"""

class Solution:
    
    # input: list of integers
    # input: nums has at least one num and reasonable enough amount to fit in mem
    # input: values of nums are integers
    
    # output: integer representing the LENGTH of the longest increasing subsequence
    
    # axiom: you can remove elements but NOT reorder elements to form a subsequence
    
    # ex. - [1, 2, 3] -> 3
    # ex. - [1, 0, -1] -> 1
    # ex. - [2, 0, 1] -> 1
    # ex. - [7, 7, 7] -> 1
    # ex. - [1, 2, 4, 3] -> [1, 2, 3] -> 3
    # ex. - [10, 5, 3, 4, 5, 100, 17] -> [3, 4, 5, 100] -> 4
    # ex. - [1, 2, 4, 13, 3] -> [1, 2, 3] -> 3
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # brute force: try every possible substring
        # time: 2^N
        # space: O(1)
        
        # sorting removes order
        
        # DP approach, using nested for loops
        # time: O(N^2)
        # space: O(N)
        
        # iterative approach, intelligently selecting nums
        # time: O(N^2)
        # space: O(N)
        # init count
        """
        subseq = [nums[0]]
        
        # iterate over list
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num > subseq[-1]:
                subseq.append(num)
            else:
                j = 0
                while subseq[j] < num:
                    j += 1
                
                subseq[j] = num
                
        # return count
        return len(subseq)
        """
        
        # above, optimized w/ binary search
        # NOTE: requires python bisect library
        subseq = [nums[0]]
        
        # iterate over list
        for i in range(1, len(nums)):
            
            num = nums[i]
            if num > subseq[-1]:
                subseq.append(num)
            else:
                # performs binary search to find index of first value in subseq
                # that's greater than or equal to num
                j = bisect_left(subseq, num)    
                subseq[j] = num
                
        # return count
        return len(subseq)