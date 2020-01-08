/*
https://leetcode.com/problems/reverse-linked-list/
time: O(N)
space: O(1)
Author: Will Cray
Date: 1/7/2020
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head)
    {
        // iterative approach
        // time - O(N), space O(1)

        if (head == NULL)
        {
            return head;
        }

        ListNode* oldNext = head->next;
        ListNode* prev = NULL;

        while (head != NULL)
        {
            // backup pointer
            oldNext = head->next;

            // update pointer
            if (prev == NULL)
            {
                head->next = NULL;
            }
            else
            {
                head->next = prev;
            }

            // iterate
            prev = head;
            head = oldNext;
        }

        return prev;
    }
};
