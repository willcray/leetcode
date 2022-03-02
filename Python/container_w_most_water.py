"""
https://leetcode.com/problems/container-with-most-water/
Author: Will Cray
Date: 3/1/2022
Time: O(N)
Space: O(1)
"""


class Solution:
    
    # input: list of integers of length n
    # input: heights are zero or more
    # n is at least two
    # height can fit on one machine's memory
    # height values are reasonably sized
    
    # output: max amount of water in area that can be contained
    
    # axiom: height of water is min between the two walls
    # axiom: amount of water is (right index - left index) * min(height[right], height[left])
    
    # ex. - [1, 2] -> 1
    # ex. - [2, 1, 2] -> 4
    # ex. - [3, 5, 3] -> 3
    # ex. - [1, 8, 5, 8, 3, 7] -> 28
    # ex. - [1, 2, 3, 0, 0] -> 2
    # ex. - [1, 3, 4, 0, 0] -> 2
    # ex. - [1,8,6,2,5,4,9,3,7] -> 40, 49
    
    
    
    def maxArea(self, height: List[int]) -> int:
        
        # brute force
        # nested loops, check area for every combination, maintain max
        # time: O(N^2)
        # space: O(1)
        
        # two pointers
        # time: O(N)
        # space: O(1)
        
        # ex. - [1, 2, 4, 3] -> 4
        # max_area = 1
        
        # init left and right pointer
        l, r = 0, len(height) - 1
        
        # init max area
        max_area = 0
        
        # loop using right pointer
        while l < r:
        
            # compute current area and compare against max
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        # return max area
        return max_area
        