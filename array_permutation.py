# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# assuming
# N is an integer within the range[1..100, 000]
# each element of array A is an integer within the range[1..1, 000, 000, 000].
# assuming N == 1 should return true

def solution(A):

    # check inputs if assumptions are void

    # 1st idea
    # time - O(N * log(N))
    # space - O(1)
    # sort A
    # iterate A with two pointers
    # check the first number is 1
    # ensure two adjacent numbers are the same
    # and the second pointer points to a number that is one
    # more than the first number
    # if not, then return 0
    # reach end, return 1

    # 2nd idea
    # time - O(N)
    # space - O(N)
    # iterate list once, storing list of bools if number was found
    found = [False] * len(A)
    for val in A:
        if val >= 0 and val < len(A):
            found[val] = True
        else:
            return 0

    # iterate list of bools, return 0 if False is encountered, else 1
    for b in found:
        if not b:
            return 0

    return 1

    # 3rd idea
    # know what the sum should be given input size N and a formula
    # sum the list, check if they're equal
    # this won't work because having the same sums doesn't mean it's a permutation
