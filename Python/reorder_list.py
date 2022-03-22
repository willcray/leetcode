"""
https://leetcode.com/problems/reorder-list/
Author: Will Cray
Date: 3/22/2022
Time: O(N)
Space: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # input: head of linked list
    # input: head is not null, list is at least length one
    # input: number of nodes can fit in single machine's mem
    
    # output: node
    
    # constraint: can't just change values
    # axiom: must reorder
    
    # ex. - 1 -> 2 -> 3, 1 -> 3 -> 2
    # ex. - 1 -> 2 -> 3 -> 4, 1 -> 4 -> 2 -> 3
    # ex. - 1 -> 2 -> 3 -> 4 -> 5, 1 -> 5 -> 2 -> 4 -> 3
    # ex. - 1, 1
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # leverage list to store nodes, iterate from both sides
        # time: O(N)
        # space: O(N)
        
        # iterate through list, send pointer to end - i
        # time: O(N^2)
        # space: O(1)
        
        # reverse second half of list, merge halves together
        # time: O(N)
        # space: O(1)
        
        # find midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of list, this moves second head to L_n,
        # and disconnects it from first half
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            
        # iterate pointer from front and to start of second half, reassigning values to specified order
        first, second = head, prev
        while second.next:
            # merge
            first.next, first = second, first.next
            second.next, second = first, second.next