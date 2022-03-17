"""
https://leetcode.com/problems/combination-sum/
Author: Will Cray
Date: 3/16/2022
Time: O(N^2)
Space: O(1)
"""

class Solution:
    
    # input: list of integers
    # input: target value to which the candidates need to sum
    # candidates is of length at least one, small enough to fit in one machine's memory
    
    # output: list of list where each sublist is a list of candidates that sum to target
    
    # axiom: unique combinations - order doesn't matter within the combination, but frequency of 
    # candidate occurence does matter
    # axiom: integers are DISTINCT
    # axiom: combs can be in any order
    # axiom: we can reuse a candidate in a comb
    
    # ex. - [2, 3, 6, 7], 7 -> [[2, 2, 3], [7]]
    # ex. - [2, 3, 5], 8 -> [[2,2,2,2], [2, 3, 3], [3, 5]]
    # ex. - [2, 3, 6, 7], 0 -> []
    # ex. - [1], 5 -> []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # recursive approach
        # time: O(2^N), where k == target, N == len(candidates)
        # space: O(K)
        
        # recursion w/ backtracking
        # time: O(N * K)
        # space: O(N * K)
        
        combs = []
        self.helper(candidates, target, 0, [], combs)
        return combs
    
    def helper(self, candidates, target, start, comb, combs):
            
        # base cases
        if target < 0: 
            return

        if target == 0: 
            combs.append(comb)
            return

        # if candidates is sorted, you can use this optimization
        # if candidates[0] > target:
            # return

        # iterate up from current index, calling recursively
        for i in range(start, len(candidates)):
            cand = candidates[i]
            self.helper(candidates, target - cand, i, comb + [cand], combs)
                
        # DP
        
        