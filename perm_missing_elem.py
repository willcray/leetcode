"""
https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
12/4/2019
Time: O(N)
Space: O(1)
"""


# assuming:
# N is an integer within the range [0..100,000]
# the elements of A are all distinct
# each element of A is an integer within the range [1..(N +1)]

def solution(A):
    # if no assumptions, do input checking here
    # check for proper input ranges, null list, negative nums

    # naive approach
    # time complexity: O(N)
    # memory complexity: O(1)
    n_1_sum = 0
    # iterate from [1,...,N+1]
    for i in range(1, len(A) + 2):
        n_1_sum += i
    # return sum(1...(N+1)) - sum(A)
    return n_1_sum - sum(A)
