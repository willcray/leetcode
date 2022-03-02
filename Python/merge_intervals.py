"""
https://leetcode.com/problems/merge-intervals/
Author: Will Cray
Date: 3/1/2022
Time: O(N log(N))
Space: O(N)
"""

class Solution:
    
    # input: list of lists of int pairs
    # input: at least one interval in intervals
    # each interval is of length two
    # each intervals values are between zero and a large number
    # num intervals is small enough to fit on one machine's memory
    
    # output: return list of lists of pairs that are merged intervals
    
    # axiom: overlapping includes equality
    # axiom: intervals are sorted via start position
    
    # ex. - [[1, 2], [2, 3]] -> [[1, 3]]
    # ex. - [[1, 2], [3, 4]] -> [[1, 2], [3, 4]]
    # ex. - [[1, 2]] -> [[1, 2]]
    # ex. - [[1,3],[2,6],[5,10],[15,18]] -> [[1, 10], [15, 18]]
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort list
        # time: O(Nlog(N)
        # space: O(N)
        
        intervals.sort()
        
        # init merged intervals list
        merged = [intervals[0]]
        
        # iterate over list
        for i in range(1, len(intervals)):
            
            start, end = intervals[i]
            
            if merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
            
        # return merged intervals list
        return merged
                