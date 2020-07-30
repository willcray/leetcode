"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
time: O(V + E)
space: O(H) = O(V)
Author: Will Cray
Date: 12/19/2019
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        def dfs(root):

            # has no children
            if not root.left and not root.right:
                return 1

            # has both children
            elif root.left and root.right:
                return max(dfs(root.left) + 1, dfs(root.right) + 1)

            # has only left child
            elif root.left and not root.right:
                return dfs(root.left) + 1

            # has only right child
            else:
                return dfs(root.right) + 1

        return dfs(root)
