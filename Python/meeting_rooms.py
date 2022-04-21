"""
https://leetcode.com/problems/meeting-rooms/
Time: O(NlogN)
Space: O(N)
Author: Will Cray
Date: 4/6/2022
"""


class Solution:
    
    # input: list of intervals (tuples of ints)
    # input: these values are zero or greater than zero
    # input: intervals list might be empty
    # output: boolean if they can attend all meetings
    
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        
        # time: O(NlogN), where N is len(intervals)
        # space: O(N), due to sort
        
        
        if len(intervals) == 0:
            return True
        
        intervals.sort()
        prev_start, prev_end = intervals[0]
        
        # iterate over sorted list
        for i in range(1, len(intervals)):
            
            curr_start, curr_end = intervals[i]
            
            # return false if there's an intersection
            if curr_start < prev_end:
                return False
            
            prev_start, prev_end = curr_start, curr_end
            
        # return true
        return True