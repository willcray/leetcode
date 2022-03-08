"""
https://leetcode.com/problems/clone-graph/
time: O(V+E)
space: O(V+E)
Author: Will Cray
Date: 3/8/2022
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    # input: Node of a connected, undirected graph
    # could be an empty graph (neighbors is None)
    # or could be a single vertext (neighbors is empty)
    # connected graph, so each 
    
    # output: new Node object representing the first vertex in the adjacency list
    # deep clone of graph
    
    # ex. - [[2], [1, 3], [2, 4], [3]]
    # ex. - [ [2], [1] ]
    
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # solution
        # BFS or DFS traversal, keeping track of visited nodes with set of node values,
        # since node values are unique
        
        # DFS will be less code and more elegant
        # BFS will be more code but likely faster in amortized time
        # choosing DFS for more practice with it
        
        # DFS and BFS
        # time: O(V + E)
        # space: O(V + E)
        
        # base case is 

        if node is None:
            return None
        
        if node.val in self.visited:
            return self.visited[node.val]
        
        # init new node with empty adj list, copied value
        node_copy = Node(node.val, [])
        
        # add current node to hash map
        self.visited[node.val] = node_copy
        
        # iterate over adjacency list
        if node.neighbors:
            node_copy.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        # return new node
        return node_copy

        
       



        