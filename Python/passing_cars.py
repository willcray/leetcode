"""
https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
12/8/2019
time - O(N)
space - O(1)
"""

# assuming:
# N is between 1 and 100,000
# all values in A are zero or one

def solution(A):

    # threshold for maximum allowed total specified in problem
    MAX_TOTAL = 1000000000

    # init total
    total = 0
    # init num zeros
    zeros = 0
    # for each car in list
    for car in A:
        # if val is zero, add to num zeros
        if car == 0:
            zeros += 1
        # else one, add num zeros to total
        else:
            total += zeros
    # truncate output if greater than 1,000,000,000
    if total > MAX_TOTAL:
        return -1
    else:
        return total
