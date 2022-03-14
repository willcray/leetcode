"""
https://leetcode.com/problems/validate-binary-search-tree/
time: O(N)
space: O(N)
Author: Will Cray
Date: 2/24/2022
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    # input is the root node of a possible BST
    # output true if BST, false otherwise
    
    # assumption: left subtree must be explicity less than and right must be explicitly greater than, not equal to
    # to form valid BST
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # iterative BFS using explicit stack
        # time: O(N)
        # space: O(N)
        
        # DFS w/ fence: 
        # time: O(N), where N is number of nodes, O(N)
        # space: O(N)
        # recursive, base case is both children are None, return true
        return self.validate(root, low=-float("inf"), high=float("inf"))
        
    def validate(self, node: Optional[TreeNode], low: float, high: float) -> bool:
        
        # base case
        if not node:
            return True

        # return false if either isn't true
        if node.val <= low or node.val >= high:
            return False
        
        # recursive call on both children that exist, logically and their results
        return (self.validate(node.right, node.val, high) and 
            self.validate(node.left, low, node.val))
        
        

    # DFS in-order traversal


    # BFS w/ explicit stack in-order traversal