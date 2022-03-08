"""
https://leetcode.com/problems/same-tree/
time: O(N)
space: O(N)
Author: Will Cray
Date: 3/8/2022
"""


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # input: two binary trees with roots p and q
    # root node is a TreeNode object
    # root node could be None
    # values of nodes are reasonable size for one machine
    # number of nodes are reasonable size for one machine
    
    # output: boolean, True if they're the same structure and values; False otherwise
    
    # ex. - [1, 2, 3]; [1, 2 , 3] -> True
    # ex. - []; [] -> True
    # see other examples
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # solution
        # need to traverse the tree
        
        # DFS or BFS
        
        # DFS
        # time: O(N), where N is number of nodes
        # space: O(N), where we could have N number of calls to the stack
        
        # BFS
        # time: O(N)
        # space: O(N), due to the stack / queue
        
        # init queue of tuples, append root nodes
        queue = deque()
        queue.appendleft((p, q))
        
        # while stack is not empty
        while queue:
            
            # pop both stacks
            p, q = queue.pop()
            
            # good if the values are the same
            if (p and q) and (p.val == q.val):
                # push children onto stack
                queue.appendleft((p.left, q.left))
                queue.appendleft((p.right, q.right))
                continue
            
            # good if they're both None
            elif not p and not q: 
                continue
            
            # otherwise, there's a mismatch
            else:
                return False
        
        return True
        