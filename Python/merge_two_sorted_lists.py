"""
https: // leetcode.com/problems/merge-two-sorted-lists/
time: O(n)
space: O(1)
Author: Will Cray
Date: 1/13/2020
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1->4->5 and 1->2->3
# 1->1->2->3->4->5


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # if both are None, return None
        if not l1 and not l2:
            return None

        # instantiate head of return list
        head = None

        # assign head to lowest value
        if l1 and l2:
            if l1.val < l2.val:
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next
        elif l1:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        # instantiate tail of return list
        tail = head

        # iterate while l1 or l2 are not none
        while l1 and l2:

            # elif both values are equal, append both to return list
            if l1.val == l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
                tail.next = l2
                l2 = l2.next

            # elif l1 is less than l2, append l1 to return list, iterate l1
            elif l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            # else l2 is less than l1, append l2 to return list, iterate l2
            else:
                tail.next = l2
                l2 = l2.next

            # iterate tail
            tail = tail.next

        # if l1 is none, append l2 to return list
        if not l1 and l2:
            tail.next = l2

        # elif l2 is none, append l1 to return list
        elif l1 and not l2:
            tail.next = l1

        # return head of merged list
        return head
