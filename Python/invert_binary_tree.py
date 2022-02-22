"""
https://leetcode.com/problems/invert-binary-tree/
Author: Will Cray
Date: 2/22/2022
Time: O(N)
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using deque for O(1) inserts
from collections import deque

class Solution:
    # input: root of a binary tree
    # input: TreeNode object
    # root could be null
    
    # output: root of inverted binary tree
    
    # ex - input: [2, 1, 3], output: [2, 3, 1]
    # ex - input: [], output: []
    # ex - input: [2], output: [2]
    # ex - input: [4, 2, 7, 1, 3, 6, 9], output: [4, 7, 2, 9, 6, 3, 1]
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # initial thought: formulaic approach manipulating indices
        # indices for a given subarray / tier start at 2^k - 1, where k is a zero-indexed depth
        # don't have direct access to list, only pointers to children, so this won't work
        
        
        # recursive solution:
        # time: O(N), where N is the number of nodes
        # space: O(N)
        
        """
        # base case
        if root is None: return None
        
        # call on left subtree
        left = self.invertTree(root.left)
        
        # call on right subtree
        right = self.invertTree(root.right)
        
        # swap left and right
        root.left = right
        root.right = left
        
        # return root
        return root
        """
        
        
        # iterative approach, using queue, resembles BFS
        # time: O(N)
        # space: O(N)
        
        if root is None: return None
        
        queue = deque([root])
        
        while queue:
            node = queue.pop()
            if node:
                # swap children
                node.left, node.right = node.right, node.left
            
                # enqueue children
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            
        return root