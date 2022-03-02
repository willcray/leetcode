"""
https://leetcode.com/problems/top-k-frequent-elements/
Author: Will Cray
Date: 3/1/2022
Time: O(N)
Space: O(N)
"""

import heapq
from collections import Counter

class Solution:
    
    # input: 
    # int array nums
    # int k
    # len nums is between 1 and a reasonable size that can fit on one machine's memory
    # k is at least 1 and less than len(nums)
    
    
    # output: k most frequently occuring numbers as a list in any order
    
    # ex. - [1, 2, 3], k = 3 -> [2, 1, 3]
    # ex. - [1, 2, 3], k = 1 -> [1]
    # ex. - [1, 1, -1, -1, 0], k = 2 -> [1, -1]
    
    # assumption: decide between vals arbitrarily in case of tie
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # priority queue / max heap
        # insert all elements into max heap
        # return top k elements via popping max
        # time: O(Nlogk)
        # space: O(N)
        
        """
        count_map = Counter(nums)

        pq = []
        heapq.heapify(pq)        
        for num, count in count_map.items():
            heapq.heappush(pq, (count * -1, num))
            
        top_k = []
        for i in range(k):
            num = heapq.heappop(pq)[1]
            top_k.append(num)
            
        return top_k
        """
    
        
        # buckets solution
        # time: O(N)
        # space: O(N)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        count_map = Counter(nums)
        
        for num, count in count_map.items():
            buckets[count].append(num)
            
        flat_list = []
        for bucket in reversed(buckets):
            flat_list += bucket
            
        return flat_list[:k]
            
        
        
        
        
        
        