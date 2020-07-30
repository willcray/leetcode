"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
Author: Will Cray
Date: 5/10/2019
Time: O(V+E)
Space: O(V)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
    # RECURSIVE
        """
        # handle empty tree
        if root == None:
            return []
        
        visited = []
        self.dfs(root, visited)
        return visited
    
    def dfs(self, root, visited):
        # base case is leaf node
        if not root.right and not root.left:
            visited.append(root.val)
            return
        
        # visit left
        if root.left != None:
            self.dfs(root.left, visited)
        
        # visit root
        visited.append(root.val)    
        
        # visit right
        if root.right != None:
            self.dfs(root.right, visited)
        return
    
        """
    # ITERATIVE
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right
        return res
        
    