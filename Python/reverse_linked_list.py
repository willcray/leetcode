"""
https://leetcode.com/problems/reverse-linked-list/
Author: Will Cray
Date: 2/22/2022
Time: O(N)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # input: node values are non-null and between -5000 and 5000, not
    # necessarily integers
    # input: list could be empty
    
    # output: returning new head to the reversed linkedlist
    
    # ex - [1, 2, 3] -> [3, 2, 1]
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # iterative solution
        # time: O(N), where N is number of nodes
        # space: O(1)
        
        #    [1, 2, 3]
        #     p
        #        c
        
        prev, curr = None, head
        
        # iterate while current node is not None
        while curr:
        
            # create copy of current node
            tmp = curr.next
            
            # reassign value of next
            curr.next = prev
            
            # iterate to copied next value
            prev = curr
            curr = tmp
            
        # return pointer to tail
        return prev
    
    
        # recursive solution (for practice):
        # time: O(N), where N is number of nodes
        # space: O(N), for N calls to the stack
        
        # base case
#         if not head or not head.next: return head
        
#         # recursive case
#         new_head = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None

#         # iterate to copied next value
#         return new_head
        
        
        
        
        