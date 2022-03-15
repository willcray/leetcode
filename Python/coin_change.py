"""
https://leetcode.com/problems/coin-change/
Author: Will Cray
Date: 3/15/2022
Time: O(N * K)
Space: O(K)
"""

class Solution:
    
    # input: list of integers, repping coin values
    # input: amount as integer that we need to hit
    # input: amount is a whole number and number of coins is at least one
    
    # output: FEWEST NUMBER of coins that you can use to hit amount; -1 if amount can't be hit
    
    # axiom: coins can be reused
    
    # ex. - [1, 5], [1] -> 1
    # ex. - [1, 5], [6] -> 2
    # ex. - [1, 5], [2] -> 2
    # ex. - [1, 5], [7] -> 3
    # ex. - [5, 10], amount: [1] -> -1
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # recursion
        # time: O(K^N), where N is len(coins)
        # space: O(K), where K is amount
        
        # recursion w/ memoization
        # don't have to recompute subproblems
        # time: O(N * K)
        # space: O(N * K)
        
        # bottom-up DP w/ memo
        # time: O(N * K)
        # space: O(K)
        
        # build memo array, initialized to 0
        memo = (amount + 1) * [float('inf')]
        memo[0] = 0
        
        # iterate over memo, starting from 1
        for target in range(1, amount + 1):
            
            # iterate over coins
            for coin in coins:

                # ensure coin is within bounds
                if coin > amount:
                    continue

                memo[target] = min(memo[target], memo[target - coin] + 1)        

        # return memo at amount
        return memo[amount] if memo[amount] != float('inf') else -1
