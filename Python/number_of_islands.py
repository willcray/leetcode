"""
https://leetcode.com/problems/https://leetcode.com/problems/number-of-islands/
Author: Will Cray
Date: 2/25/2022
Time: O(N * M)
Space: O(N * M)
"""


class Solution:
    # input: m x n matrix of strs, only 1's and zeros
    
    # output: number of islands
    
    # axioms: water surrounds the grid
    # land doesn't connect on diagonals
    # islands can be larger than just one position on the grid
    
    
    # Union Find / Disjoint Sets w/ path compression and rank
    # Time: O(N * M)
    # Space: O(N * M)
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n, m = len(grid), len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(n) for j in range(m))
        parent = [i for i in range(n * m)]
        rank = n * m * [0]
        
        def find(x) -> int:
            # if x isn't the parent, find the parent
            if parent[x] != x:
                return find(parent[x])
            
            return parent[x]
                
            
        # union with rank
        def union(x, y) -> None:
            x_root, y_root = find(x), find(y)
            if x_root == y_root: return 
            
            if rank[x_root] < rank[y_root]:
                x_root, y_root = y_root, x_root
                
            parent[y_root] = x_root
            rank[x_root] = max(rank[x_root], rank[y_root] + 1)
            self.count -= 1
                
        for i in range(n):
            for j in range(m):
                
                if grid[i][j] == '0':
                    continue
                    
                index = (i * m) + j
                if j < m - 1 and grid[i][j + 1] == '1':
                    union(index, index + 1)
                if i < n - 1 and grid[i + 1][j] == '1':
                    union(index, index + m)
        
        return self.count
    
    
    # BFS:
    # Time: O(N * M)
    # Space: O(N * M)
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # init count
        num_islands = 0
        
        # n is at least length one, so this is safe
        n, m = len(grid), len(grid[0])
        
        # iterate over grid
        for i in range(n):
            for j in range(m):
        
                # if 1
                if grid[i][j] =='1':
                    # add one to island count
                    num_islands += 1
                    self.BFS(grid, i, j)
        
        # return count
        return num_islands
    
    
    def BFS(self, grid: List[List[str]], r: int, c: int):
        # redefining n, m, and stack reduces number of needed params, 
        # resulting cleaner code but sacrificing speed
        n, m = len(grid), len(grid[0])
        stack = []
        
        # push onto stack
        stack.append((r, c))
        # while stack isn't empty
        while stack:
            # pop from stack
            r, c = stack.pop()
            # mark as visited
            grid[r][c] = '0'
            # push all non-zero neighbors onto stack
            if r - 1 >= 0 and grid[r - 1][c] == '1': stack.append((r - 1, c)) # left
            if c - 1 >= 0 and grid[r][c - 1] == '1': stack.append((r, c - 1)) # up
            if c + 1 < m and grid[r][c + 1] == '1': stack.append((r, c + 1)) # down
            if r + 1 < n and grid[r + 1][c] == '1': stack.append((r + 1, c)) # right
    """
        
    
    
    # DFS:
    # Time: O(N * M)
    # Space: O(N * M)
    """
    def numIslands(self, grid: List[List[str]]) -> int:
    
        num_islands = 0
        # iterate over grid
        for i in range(len(grid)):
            
            for j in range(len(grid[i])):
            
                # if 1
                if grid[i][j] == '1':
                    num_islands += 1
                    # iterate each direction until water (zero)
                    self.searchForWater(grid, i, j)

        return num_islands
    
    
    def searchForWater(self, grid: List[List[str]], i: int, j: int):
        
        n = len(grid)
        # we know n will be at least of size one
        m = len(grid[0])
        
        # base case 
        if (i < 0 or i >= n or
            j < 0 or j >= m or
            grid[i][j] == '0'):
            return
        
        else:
            # mark as visited
            grid[i][j] = '0'
            # call recursively on neighbors
            self.searchForWater(grid, i - 1, j) # left
            self.searchForWater(grid, i, j - 1) # up
            self.searchForWater(grid, i + 1, j) # right
            self.searchForWater(grid, i, j + 1) # down
        
        return
    """
    
    