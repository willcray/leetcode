"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
Author: Will Cray
Date: 3/9/2022
Time: O(N)
Space: O(N)
"""

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # input: root TreeNode representing a binary tree
    # input: root node could be None
    # input: number of nodes can fit in one machine's memory

    # output: list of lists of ints where each sublist represents the value for each node of each
    # level from left to right
    # output: sublists exclude None values
    
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # DFS
        # time: O(V + E) or O(N)
        # space: O(V + E) or O(N)
        
        # BFS
        # time: O(V + E) or O(N)
        # space: O(V + E) or O(N)
        res = []
        
        # init queue w/ root + depth of 0
        q = deque()
        if root: q.appendleft((root, 0))
        
        # while queue isn't empty
        while q:
            
            # pop from q
            node, depth = q.pop()
            
            # check if level in result list, insert into level list corresponding to depth
            # TODO: double check for off by one's
            if len(res) <= depth:
                res.append([])
                
            # append value of current node to list for that level
            res[depth].append(node.val)
            
            # enqueue non-None children w/ current depth + 1
            if node.left: q.appendleft((node.left, depth + 1))
            if node.right: q.appendleft((node.right, depth + 1))
            
        # return result list
        return res
        