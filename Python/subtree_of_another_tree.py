"""
https://leetcode.com/problems/subtree-of-another-tree/
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
class Solution:
    
    # input: the root node of a tree, a node that could be a subtree
    # input: there are at least one node in each tree
    # input: nodes can be null if other, non-null nodes exist at their depth
    
    # output: boolean, does subRoot represent a subtree of the root tree
    
    # axiom: a proper subtree must match the root tree exactly in both structure 
    # and value from the subRoot down
    
    # ex - root: [1, 2, 3], subRoot: [1, 2, 3] -> True
    # ex - root: [1, 2, 3], subRoot: [1, None, 3] -> False
    # ex - root: [1], subRoot: [2] -> False
    # ex - root: [1, 2], subRoot: [2] -> False
    # ex - root: [1, 2], subRoot: [2] -> False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # solution: DFS
        # time: O(N), where N is the number of nodes. More specifically, it's O(V + E)
        # space: O(N), because we have as many calls to the stack as we do height
        # of the tree, which could be N nodes tall.
        
        # base case, root being none
        if root is None: return False
        
        # check for match at current depth
        if self.isMatch(root, subRoot): return True
        
        # perform DFS on subtrees
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
            
    
    def isMatch(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root or not subRoot:
            return root == subRoot
        
        # ensure that the values and subtrees are equal
        return (root.val == subRoot.val and
                self.isMatch(root.left, subRoot.left) and
                self.isMatch(root.right, subRoot.right))
        
        
            
            
        
        
        
                
        

        