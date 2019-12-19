"""
https://leetcode.com/problems/sum-of-left-leaves
Time: O(V + E)
Space: O(N)
Author: Will Cray
Date: 12/18/2019
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def dfs(root, left=False):
            # left leaf
            if not root:
                return 0

            elif not root.left and not root.right and left:
                return root.val

            elif not root.left and not root.right:
                return 0

            else:
                return dfs(root.left, True) + dfs(root.right, False)

        return dfs(root, False)
