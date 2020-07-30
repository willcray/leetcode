"""
https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
12/4/2019
Time: O(N*M)
Space: O(1)
"""

# assuming
# non-empty input array A
# N and M are integers within the range [1..100,000];
# each element of A is an integer within the range [1..N + 1]

def solution(N, A):

    # naive approach:
    # time - O(M * N)
    # space - O(1) if excluding return list, else O(N)


    # instantiate counters
    counters = [0] * N
    # Keep track of the max val so there's no need to find it
    curr_max = 0

    # iterate A and apply operation corresponding to current value in A
    for val in A:

        # if val <= N, add one to the counter at val index
        if val <= N:
            # where first counter is index zero
            # again assuming that all vals in A are >= 1
            counters[val - 1] += 1
            # update max val if greater than current max val
            if counters[val - 1] > curr_max:
                curr_max = counters[val - 1]

        # else A is N + 1, apply max counter
        else:
            # max counter iterates N and updates each value to max val
            for i in range(N):
                counters[i] = curr_max

    return counters

    """
    # may be able to break the max counter update loop out for a O(M) runtime by keeping track of max vals and their number

    counters = [0] * N
    # Keep track of the max val so there's no need to find it
    curr_max = 0
    maxes = []

    # iterate A and apply operation corresponding to current value in A
    for val in A:

        # if val <= N, add one to the counter at val index
        if val <= N:
            # where first counter is index zero
            # again assuming that all vals in A are >= 1
            counters[val - 1] += 1
            # update max val if greater than current max val
            if counters[val - 1] > curr_max:
                curr_max = counters[val - 1]

        # else A is N + 1, apply max counter
        else:
            # max counter iterates N and updates each value to max val
            maxes.append(curr_max)

    for m in maxes:
        # add to each value except at the value at
        # which the max was held

    return counters
    """
