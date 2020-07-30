"""
https://leetcode.com/problems/linked-list-cycle/
Author: Will Cray
Date: 4/26/2019
Time: O(n)
Space: O(1)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        if not head.next:
            return False
        
        # while loop
        while(True):
            # check if head has not been visited
            if head.val != "v":
                # if not visited and next is not None, mark as visited, update head
                if head.next:
                    # marks current node as visited
                    head.val = "v"
                    # update head to next node in list
                    head = head.next
                # if not visited and next is None, return False
                else:
                    return False
            # if visited, return True
            else:
                return True
        
        """
        # set solution - O(N) time, O(N) space
        s = set()
        while(True):
            if head.next in s:
                return True
            elif head.next is None:
                return False
            else:
                s.add(head)
                head = head.next
        """