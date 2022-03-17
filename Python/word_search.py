"""
https://leetcode.com/problems/word-search/
Author: Will Cray
Date: 3/17/2022
Time: O(M * N)
Space: O(K)
"""

class Solution:
    
    # input: m x n grid of characters
    # input: word, string
    # m, n, len(word) are at least one
    # grid size is small enough to fit in memory, as is word length
    
    # output: true if word is present in grid, else false
    
    # constraint: character in cell cannot be used twice in word construction
    # constraint: next char used must be left, up, right, down adjacent cells
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # BFS or DFS
        # time: O(M * N)
        # space: O(len(word))
        
        # we know m is at least one, so this is afe
        m, n = len(board), len(board[0])
        
        # iterate over each cell
        for i in range(m):
            for j in range(n):
                
                # call DFS on each cell, return true if DFS returns true
                if self.DFS(board, m, n, word, 0, i, j):
                    return True
                
        # return false because no search was successful
        return False
        
        
    # create helper function that performs DFS
    def DFS(self, board: List[List[str]], m: int, n: int, word: str, word_idx: int, i: int, j: int) -> bool:
        
        # base cases
        # check if char is what we're looking for
        # backtrack
        if word[word_idx] != board[i][j]:
            return False
        
        # check if it's successful search (final char)
        if word_idx == len(word) - 1:
            return True
        
        # mark as visited, save value to replace later
        tmp = board[i][j]
        board[i][j] = "#"
        
        # call on neighbors
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            
            new_i, new_j = i + x, j + y
            # return or of all neighbors if in bounds
            if 0 <= new_i < m and 0 <= new_j < n:
                if self.DFS(board, m, n, word, word_idx + 1, new_i, new_j):
                    return True
        
        # replace on board for future calls
        board[i][j] = tmp
        
        return False