"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
time: O(N)
space: O(1)
Author: Will Cray
Date: 1/17/2020
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sanitize input
        # assuming values entered are positive integers

        # [2, 1, 2, 1, 0, 1, 2]
        #              b
        #                    s

        if len(prices) < 2:
            return 0

        buy = 0
        best_profit = 0
        for sell in range(1, len(prices)):
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = sell
            elif profit > best_profit:
                best_profit = profit

        return best_profit
