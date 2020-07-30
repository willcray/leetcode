"""
https://leetcode.com/problems/course-schedule-ii/
Author: Will Cray
Date: 5/8/2019
Time: O(V+E)
Space: O(V+E)
"""

from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # create visited array with n indices
        self.visited = [0] * numCourses
        # create stack
        self.stack = []
                
        # create graph
        self.adj_list = defaultdict(list)
        for dest, src in prerequisites:
            self.adj_list[src].append(dest)
              
        # for each unvisited vertex, call recursive function
        for i in range(numCourses):
            if not self.dfs(i):
                return []
        # return stack (which is stored as a list in python)
        return self.stack[::-1]
        
    # recursive function
    def dfs(self, i):
              
        if self.visited[i] == -1:
            return False
              
        if self.visited[i] == 1:
            return True
        
        # start recursion
        self.visited[i] = -1
        # for each unvisited neighbor, call function recursively
        for dest in self.adj_list[i]:
            if not self.dfs(dest):
                return False
        # when no unvisited neighbors
        self.stack.append(i)
        self.visited[i] = 1
        return True

                    