"""
https://leetcode.com/problems/insert-interval/
Author: Will Cray
Date: 2/23/2022
Time: O(N)
Space: O(1)
"""


class Solution:
    
    # input: 
    # list of list of ints
    # newInterval, list of ints, representing a new interval
    
    
    # output:
    # intervals (list of list of ints) with newInterval inserted
    # merge all intervals that overlap / touch a value in newInterval
    
    # constraints: 
    # each pair is sorted via the start or first number in the interval
    # interval numbers greater than or equal to zero and are small enough to fit in mem
    # intervals could be of length zero, but will also be reasonably sized
    # guaranteed that each interval has two nums in it
    # start and end could be equal, but start will never be greater than end
    
    # ex. - [] -> output: []
    # ex. - [[1, 2], [2, 3]], [2, 2] -> output: [[1, 3]]
    
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # time: O(N)
        # space: O(1)
        
        # create return list
        res = []
        
        new_start, new_end = newInterval
        
        # loop over intervals
        for idx, (i_start, i_end) in enumerate(intervals):
            
            # no overlap -- interval to be inserted is after 
            # current interval's end
            if i_end < new_start: 
                res.append([i_start, i_end])
            
            # no overlap -- interval to be inserted is before
            # current interval's start
            elif new_end < i_start: 
                res.append([new_start, new_end])
                # can return earlier
                return res + intervals[idx:]
                
            # overlap
            elif i_end >= new_start or i_start <= new_end:
                    
                new_start = min(new_start, i_start)
                new_end = max(new_end, i_end)
        
        # if it hasn't returned yet, then new interval was never appended, so append it
        res.append([new_start, new_end])
            
        # return list
        return res
        