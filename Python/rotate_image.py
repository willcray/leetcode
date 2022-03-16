"""
https://leetcode.com/problems/rotate-image/
Author: Will Cray
Date: 3/16/2022
Time: O(N^2)
Space: O(1)
"""

class Solution:
    
    # input: 2D square matrix, list of lists of int
    # input: matrix can fit in mem, n > 0
    
    # output: none
    
    # axiom: rotate matrix by 90 degrees in place
    
    # ex. - [[1]]
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # solution: rotate groups of four cells
        # time: O(N ^2)
        # space: O(1)
        
        # better solution: transpose, then reflect
        # time: O(N ^ 2)
        # space: O(1)
        
        n = len(matrix)
        
        # flips across diagonal
        def transpose(matrix: List[List[int]]) -> None:
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        # flips about y-axis (reverses each row)
        def reflect(matrix: List[List[int]]) -> None:
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
            
            
        transpose(matrix)
        reflect(matrix)
            