"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
Author: Will Cray
Date: 2/22/2022
Time: O(N)
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # input: three TreeNode objects, root, p, q
    
    # output: TreeNode that represents the LCA of p and q, this can include p or q
    
    # constraints: 
    # p and q will exist in the BST, and will never be equal
    # p will not equal q
    # at least two nodes in the tree
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        """
        # recursive solution
        # DFS-like approach
        # time: O(N) or O(V + E), where N or V are number of TreeNodes
        # space: O(N) or O(V + E)
        
        # recursively call on either subtree, looking for value between p and q
        # p and q are in left subtree
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        
        # p and q are in right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # base case is when you've found the LCA
        # this is when root is between p and q
        else: 
            return root
        """
        
        # iterative solution
        # time: O(N) or O(V + E)
        # space: O(N) or O(V + E)
        
        while root:
            # p and q are in left subtree
            if p.val < root.val and q.val < root.val: 
                root = root.left
        
            # p and q are in right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            else:
                return root
        
        