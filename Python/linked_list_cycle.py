"""
https://leetcode.com/problems/linked-list-cycle/
Author: Will Cray
Date: 2/22/2022
Time: O(N)
Space: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # input: linked list containing ListNode objects
    # list could be empty
    
    # output: boolean, true if there is a cycle, false otherwise
    
    # ex - [1, 2, 3], pos = 1, output = true
    # ex - [], pos = -1, output = false
    # ex - [1], pos = -1, output = false
    # ex - [1, 2], pos = -1, output = false
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # initial solution - iterative using set
        # time: O(N), where N is number of nodes
        # space: O(N), due to the hash table
        
        """
        visited = set()
        
        # iterate each node
        while head:
            
            # return true if we've ever seen a node before
            if head in visited: return True
            
            # add node to a visited set
            visited.add(head)
            
            # step to next node
            head = head.next
            
        # return false if you finish iterating without revisiting
        return False
        """

    
        # Floyd's Cycle Finding Algo
        # time: O(N)
        # space: (1)
        
        if head is None: return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None: 
                return False
            fast = fast.next.next
            slow = slow.next
        
        return True
    
        