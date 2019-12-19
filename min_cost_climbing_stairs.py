"""
https://leetcode.com/problems/min-cost-climbing-stairs/
Time: O(N)
Space: O(1)
Author: Will Cray
Date: 12/18/2019
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # iterate until we can step to the top
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[-2], cost[-1])
