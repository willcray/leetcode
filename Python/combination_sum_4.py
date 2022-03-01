"""
https://leetcode.com/problems/combination-sum-iv/
Author: Will Cray
Date: 2/28/2022
Time: O(N * M)
Space: O(N)
"""

class Solution:
    
    # input: list of nums, that are integers
    # target int
    # at least one num in nums, target is valid int
    # nums is of reasonable length for one machine
    # all nums are positive
    # all nums are unique
    
    # output: number of permutations of any amount numbers that add up to target
    
    # NOTE: all nums are unique, could drive optimizations
    
    # NOTE: you can repeatedly use an integer
    
    # ex: [1, 2] , target = 3,
    # (1, 1, 1), (1, 2), (2, 1) -> 3
    
    # ex [9], target = 20 -> 0
    
    # ex [10, 13, 14], target = 2 -> 0
    
    # ex. - memo = [0, 1, 2, ]
    # [1, 1], [2, 1], [1, 2] target = 2
    # target = 3, [1, 1, 1], [2, 1], [1, 2], [3]
    # target = 4 

    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # recursive backtracking
        # time: O(2^N), where N is len(nums)
        # space: O(M), where M is the value of target
        
        
        # optimize with memoization
        # time: O(N * M)
        # space: O(M)
        
        
        # bottom DP approach
        # time: O(N * M)
        # space: O(M)
        memo = (target + 1) * [0]
        memo[0] = 1
        
        # start at 1, iterate to target value
        for temp_target in range(1, target + 1):
            
            for num in nums:
                if temp_target - num >= 0: 
                    memo[temp_target] += memo[temp_target - num]
            
        return memo[target]