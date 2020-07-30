"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
Time: O(V + E)
Space: O(H) = O(V)
Author: Will Cray
Date: 12/19/2019
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def dfs(root):
            if not root:
                return []

            elif len(root.children) == 0:
                return [root.val]

            traversal = []
            for child in root.children:
                traversal += dfs(child)

            return traversal + [root.val]

        return dfs(root)










