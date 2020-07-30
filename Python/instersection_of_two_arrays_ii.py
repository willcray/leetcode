"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
time: O(N)
space: O(N)
Author: Will Cray
Date: 1/6/2020
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # solution 1:
        # nested for loop inserting on each duplicate into new return array
        # keep a visited set, skip number if already visited
        # time - O(N^2), space - O(N)

        # solution 2:
        # keep a dictionary of number of occurences for both lists

        dict1 = {}

        for num in nums1:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1

        ret_list = []

        for num in nums2:
            if num in dict1 and dict1[num] > 0:
                ret_list.append(num)
                dict1[num] -= 1

        return ret_list


