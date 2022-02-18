"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
time: O(N)
space: O(1)
Author: Will Cray
Date: 2/18/2022
"""

class Solution:
    # input: array of integers
    # input: whole numbers (integers 0 or greater)
    # input: len(prices) will be at least one or more
    # input: prices isn't necessarily sorted
    
    # output: int that reps the max profit that can be made
    # output: if you can't make a profit, return zero
    
    # constraint: sales price can only occur after buy price
    
    # ex - input: [2] - output: 0
    # ex - input: [2, 1, 4] - output: 3
    # ex - input: [2, 2] - output: 0
    
    def maxProfit(self, prices: List[int]) -> int:
        
        # brute force: nested for loop, two pointers, maintain a max profit,
        # which would be initialized at zero
        # time: O(n^2), where n is len(prices)
        # space: O(1)
        
        # better solution: create hash map price -> index, sort map, 
        # compute difference between the first and last element, checking to ensure
        # the sale price's index is greater than the buy prices index
        # time: O(nlog(n))
        # space: O(1)
        
        # best solution: two pointers, one loop
        # maintain a max profit value, initialized at zero
        max_profit = 0
        buy = 0
        
        # iterate with two pointers
        for sell in range(1, len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > max_profit:
                max_profit = profit
            if profit <= 0:
                buy = sell
            
        return max_profit
