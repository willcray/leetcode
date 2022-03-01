"""
https://leetcode.com/problems/jump-game/
Author: Will Cray
Date: 2/28/2022
Time: O(N * M)
Space: O(1)
"""

class Solution:
    
    # input: list of integers
    # nums are between zero and a large, positive number
    # at least one eleemnt in nums
    
    # output: boolean, true if you can reach the last index (last element in the list)
    
    # axiom: each num represents the MAX jump length
    
    # ex. - [1, 2, 3] -> True
    # ex. - [0, 1] -> False
    # ex. [9] -> True
    # ex. [2, 0, 3, 0, 1] -> False
    
    def canJump(self, nums: List[int]) -> bool:
        
        # BFS, not quite as fast amortized as DFS
        
        # DFS with backtracking
        # Time: O(2^N), where N is the len of nums, M is the largest num in nums
        # Space: O(N), 
        
        # could optimimize with memoization to avoid recomputing answer at a given index
        # this is a top-down DP approach
        
        """
        # DP solution
        # time: O(N*M)
        # space: O(N)
        
        # [False, False, False, False, True]
        
        # [2, 3, 1, 1, 4]
        
        # init memo array, storing true in index zero
        memo = len(nums) * [False]
        memo[-1] = True
        # iterate through list in reverse, starting at second to last index
        # i = 0 is end of nums
        for i in range(len(nums) - 2, -1, -1):
            
            # iterate and decrement the value of num
            furthest_jump = min(nums[i], len(nums) - 1 - i)
            
            for jump in range(1, furthest_jump + 1):
                    
                # check if you can get to end, if so, store True, break back to for loop    
                if memo[i + jump]:
                    memo[i] = True
                    break
            
        # return memo at index zero
        return memo[0]
        """
        
        # DP solution w/o memoization
        # we only ever use the left-most True position
        # time: O(N * M)
        # space: O(1)
        
        last_true = len(nums) - 1
        
        # iterate through list in reverse, starting at second to last index
        for i in range(len(nums) - 2, -1, -1):
            
            if (i + nums[i] >= last_true): last_true = i
                
        return last_true == 0
        
        
        
            