"""
https://leetcode.com/problems/course-schedule/
time: O(V+E)
space: O(V+E)
Author: Will Cray
Date: 1/13/2020
"""

# example [0, 1]
# you have to take course 1 before you take course zero
# DAG where adjacent nodes are prereqs
# is it possible to visit all nodes

# the only situation where the result is false is when a cycle exists

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # check input
        if numCourses == 0 or len(prerequisites) == 0:
            return True

        # construct graph
        graph = {i: set() for i in range(numCourses)}
        indegrees = {i: 0 for i in range(numCourses)}

        # add prereqs to graph
        for course, prereq in prerequisites:
            graph[course].add(prereq)
            indegrees[prereq] += 1

        visited = set()
        q = collections.deque()

        for course in indegrees:
            if indegrees[course] == 0:
                q.append(course)

        while len(q) > 0:

            course = q.popleft()
            visited.add(course)

            for prereq in graph[course]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    q.append(prereq)

        return len(visited) == numCourses








