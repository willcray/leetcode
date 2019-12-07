"""
https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
12/7/2019
time - O(N)
space - O(N)
"""

# assuming:
# N is an integer within the range [1, ..., 100,000]
# A contains only integers from [-100,000, ... , 100,000]

def solution(A):

    # 1st Solution
    # time - O(N*log(N))
    # space - O(1)
    # sort the list, iterate until you reach
    # first positive, non-zero value, return value
    # if you reach the end, return 1

    # 2nd Solution
    # time - O(N)
    # space - O(N)
    # keep another marker list of bools
    markers = [False] * (len(A) + 1)
    # iterate through list
    for val in A:
        # if current val > 0, add "True" in marker list
        # at index of that val
        if val > 0 and val < len(markers):
            markers[val] = True

    # iterate through marker list
    # ignoring value at 0, it will be False
    for i in range(1, len(markers)):
        # return index of first "False"
        if markers[i] == False:
            return i

    # this is the case where every value in the list is
    # positive and sequential
    return len(A) + 1


    # 3rd Solution
    # use a set instead of a marker list
    # same performance in time and space as 2nd Solution
