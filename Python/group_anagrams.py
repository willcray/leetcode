"""
https://leetcode.com/problems/group-anagrams/
time: O(N*Mlog(M))
space: O(N)
Author: Will Cray
Date: 1/14/2020
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # solution 1 - create sets for each string, compare sets
        # time - O(N*Mlog(M)), space - O(N)

        # solution 2 - use a dict with a mapping of set() -> index of output array
        output = []
        d = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in d:
                # store the index in the output array of the
                # new anagram
                d[sorted_s] = len(output)
                output.append([s])
            else:
                out_index = d[sorted_s]
                output[out_index].append(s)

        return output

