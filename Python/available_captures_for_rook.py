"""
https://leetcode.com/problems/available-captures-for-rook
Author: Will Cray
Date: 4/24/2019
Time: O(1)
Space: O(1)
"""

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # assuming valid input with valid dimensions
        I = 0
        J = 0
        # iterate matrix until you find 'R', store those values in I, J
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 'R':
                    I = i
                    J = j
                    break
        # starting at the location of 'R'
        i = I
        j = J
        sum = 0
        # iterate all four directions within the bounds of the matrix
        while i > 0:
            i -= 1
            if board[i][J] != '.':
                if board[i][J] == 'p':
                    sum += 1
                break
        i = I
        while i < len(board) - 1:
            i += 1
            if board[i][J] != '.':
                if board[i][J] == 'p':
                    sum += 1
                break
        while j > 0:
            j -= 1
            if board[I][j] != '.':
                if board[I][j] == 'p':
                    sum += 1
                break
        j = J
        while j < len(board) - 1:
            j += 1
            if board[I][j] != '.':
                if board[I][j] == 'p':
                    sum += 1
                break
        
        return sum