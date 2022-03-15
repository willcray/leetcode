"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Author: Will Cray
Date: 3/1/2022
Time: O(N)
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # input: two arrays of integers
    # values are values for nodes
    # lists are at least one node long and of a reasonable enough size to fit in memory of standard machine
    # lists are same length
    # the lists represent the valid preorder and inorder traversals of the same values / nodes
    # all values are unique
    
    # output: the root node of a binary tree
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # recursive approach using preorder, have to cross reference both arrays
        # time: O(N), where n length of preorder or inorder
        # space: O(N), recursive calls
        
        inorder_lookup = {}
        for i, num in enumerate(inorder):
            inorder_lookup[num] = i
        
        # preorder gives us the value of root
        pre_iter = iter(preorder)
        
        def buildSubtree(start, end):
            if start > end:
                return None
            
            # iterate to next root
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            idx = inorder_lookup[root_val]
            
            # call recursively on subtrees
            root.left = buildSubtree(start, idx - 1)
            root.right = buildSubtree(idx + 1, end)
            
            return root
        
        return buildSubtree(0, len(inorder) - 1)
        
    
        