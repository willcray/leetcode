"""
https://leetcode.com/problems/sliding-window-maximum/
Author: Will Cray
Date: 5/8/2019
Time: O(N)
Space: O(k)
"""


from collections import deque
class Solution:
    def add_to_dq(self, dq, nums, i):
        while len(dq) and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        return
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:       
        dq = deque()
        output = []
        # fill deque with index of max number for the first window, append to output
        for i in range(k):
            self.add_to_dq(dq, nums, i)
        
        start, end = 0, k-1
        while end < len(nums) and nums:
            while True:
                if dq[0] >= start:
                    output.append(nums[dq[0]])
                    break
                else:
                    dq.popleft()
            start += 1
            end += 1
            if end < len(nums):
                self.add_to_dq(dq, nums, end)
        return output
