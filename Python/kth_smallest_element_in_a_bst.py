"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
time: O(N) for the worst case with an unbalanced tree, O(logN) for balanced
space: O(N) for unbalanced tree, log(N) for balanced
Author: Will Cray
Date: 3/14/2022
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    # input: BST root, which is a TreeNode object
    # input: integer k, 1-indexed
    # k will be at least one and less than or equal to number of nodes
    # at least one node in tree
    # values in each node are whole numbers and ARE UNIQUE
    
    # output: the value of the kth smallest value, 1-indexed
    
    
    # ex - [2, 1, 1] k = 2 -> invalid example because values are unique
    # ex - [3,1,4,null,2], k = 1 -> 1
    # ex - [3,1,4,null,2], k = 2 -> 2
    # ex - [3,1,4,null,2], k = 4 -> 4
    # ex - [5,3,6,2,4,null,null,1], k = 3
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # solution:
        # in-order iterative traversal
        # enables breaking out early rather than traversing entire tree
        # time: O(N) for the worst case with an unbalanced tree, O(logN) for balanced
        # space: O(N) for unbalanced tree, log(N) for balanced
        
        # init stack
        stack = []
        
        while True:
            # iterate to bottom of left subtree
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            k -= 1
            # return value if it's the kth smallest
            if k == 0:
                return root.val
        
            # reset root to right subtree
            root = root.right
        
        
        
        """
        # DFS
        # time: O(N) for entire tree traversal
        # space: O(N) to store traversal
        
        def DFS(root) -> None:

            if not root: 
                return []
            else:
                return DFS(root.left) + [root.val] + DFS(root.right)

        
        traversal = DFS(root)
        return traversal[k - 1]
        """
        