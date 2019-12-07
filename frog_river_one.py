"""
https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
12/7/2019
time - O(N)
space - O(N)
"""

# assuming:
# array A is non-empty
# N and X are integers within the range [1..100,000]
# each element of array A is an integer within the range [1..X]
#


def solution(X, A):

    # frog can't pass if len(A) < X
    if len(A) < X:
        return -1

    # 1st approach
    # time - O(len(A)) -> O(N)
    # space - O(X) -> O(N)

    # init set
    s = set()
    # iterate list A
    for i in range(len(A)):
        # if not in set and <= X, add to set
        if A[i] <= X and A[i] not in s:
            s.add(A[i])
            # if size of set == X we have all the values we need
            if len(s) >= X:
                # return current index
                return i

    # return -1
    return -1


    # second approach
    # time - O(len(A)) -> O(N)
    # space - O(X) -> O(N)
    # derive formula for x + x - 1 + x - 2 + .... + x - (x - 1)
    # store as total variable
    # decrement from this total whenever you a number less than X
    # for the first time
    # return index when total is zero

    # 3rd approach
    # time - O(N*log(N))
    # space - O(1)
    # sort list, return index of first occurence of X
    # return -1 if never encountered
