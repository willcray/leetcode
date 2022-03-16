"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
Author: Will Cray
Date: 3/16/2022
Time: O(M * N)
Space: O(M * N)
"""

class Solution:
    
    # input: heights, m x n grid of integer values
    # heights are greater than or equal to zero
    # m and n are at least one, grid is small enough to fit in one machine's memory
    
    # output: 2D list of coordinates, repping if water can flow to BOTH pacific and atlantic
    # from that pair of coordinates
    # the presence of the coordinates, is boolean for water can flow to both oceans
    
    # axiom: water can't flow diagonally
    # axiom: water can flow when next cell's height is less than or equal to current cell's height
    
    # checking to see at each coordinate that water can flow to BOTH oceans
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # recursion
        # time: O(N^2 * M^2)
        # space: O(N^2 * M^2)
        
        # DFS w/ memoization... we could also use BFS
        # time: O(M * N)
        # space: O(M * N)
        
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # set to mark which cells are able to reach each ocean
        pacific_reachable, atlantic_reachable = set(), set()
        
        def DFS(i, j, reachable):
            
            # this cell is reachable, since we initiated the search from each ocean
            reachable.add((i, j))
            
            for (x, y) in directions:

                new_row, new_col = i + x, j + y
                
                # invalid bounds check
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue
                
                # skip if already visited
                if (new_row, new_col) in reachable:
                    continue
                
                # flowability check, skip if can't flow to next cell
                # we started at the ocean, so we need to check if
                # the next cell's height is greater or equal to
                if heights[new_row][new_col] < heights[i][j]:
                    continue
                
                DFS(new_row, new_col, reachable)
                
        
        # start DFS from each cell adjacent to oceans
        for i in range(m):
            DFS(i, 0, pacific_reachable)
            DFS(i, n - 1, atlantic_reachable)
        for i in range(n):
            DFS(0, i, pacific_reachable)
            DFS(m - 1, i, atlantic_reachable)
        
        # perform set intersection
        return list(pacific_reachable.intersection(atlantic_reachable))