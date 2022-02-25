"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Author: Will Cray
Date: 2/24/2022
Time: O(N)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    # input: head of linked list, ListNode object
    # integer n repping the node FROM THE END to be removed
    
    # output: head of the linked list with the nth node removed
    
    # constraints: at least one node (head is non null)
    # constraints: n (indexing from 1) will always be a node in the linked list
    
    # ex: [1, 2, 3], n = 1 -> [1, 2]
    # ex: [1, 2, 3], n = 2 -> [1, 3]
    # ex: [1], n = 1 -> []
    # ex: [2, 1, 2], n = 3 -> [1, 2]
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # first attempt: two pass, optimal worst time complexities but not optimal amortized
        # time: O(N)
        # space: O(1)
        
        # second attempt: one pass
        # time: O(N)
        # space: O(1)
        
        fast = slow = head
        for _ in range(n):
            fast = fast.next
            
        if fast is None:
            return head.next
        
        # iterate until first reaches the end, curr will be on the node to remove
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        
        return head
    
    
        