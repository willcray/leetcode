"""
https://leetcode.com/problems/spiral-matrix/
Time: O(M * N)
Space: O(1)
Author: Will Cray
Date: 3/29/2022
"""


class Solution:
    
    # input: 2D list of integers, being a matrix, not necessarily square
    # input: matrix is small enough for one machine's memory
    # both dims are at least one
    
    # output: list of integers in spiral order
    
    # axiom: definition of spiral order
    
    # ex - on the side
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # iterative with four loops, one larger, external loop, where larger loop maintains bounds
        # time: O(m * n)
        # space: O(1)
        
        # init return list
        spiral = []
        
        # bounds for i and j (inclusive)
        min_i, min_j = 0, 0
        max_i, max_j = len(matrix) - 1, len(matrix[0]) - 1
        
        # loop while both bounds don't intersect
        while min_i <= max_i and min_j <= max_j:
            
            # increment j to right bound (inclusive)
            for j in range(min_j, max_j + 1): 
                spiral.append(matrix[min_i][j])
            
            min_i += 1
            
            # increment i to bottom bound (inclusive)
            for i in range(min_i, max_i + 1): 
                spiral.append(matrix[i][max_j])
            
            max_j -= 1
            
            if min_i <= max_i:
                # decrement j to left bound (inclusive)
                for j in range(max_j, min_j - 1, -1): 
                    spiral.append(matrix[max_i][j])

            max_i -= 1
            
            if min_j <= max_j:
                # decrement i to top bound
                for i in range(max_i, min_i - 1, -1): 
                    spiral.append(matrix[i][min_j])
                
            min_j += 1
            
            
        return spiral
        
        
        # recursive
        # time: O(m * n)
        # space: O(m * n), maintain bounds or visited set
        
        # iterative via marking each cell as visited
        # time: O(m * n)
        # space: O(1)
        
        