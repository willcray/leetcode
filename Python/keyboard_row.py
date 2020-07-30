"""
https://leetcode.com/problems/keyboard-row/
Author: Will Cray
Date: 4/17/2019
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # create set for each row
        zero = set(["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"])
        one = set(["A", "S", "D", "F", "G", "H", "J", "K", "L"])
        two = set(["Z", "X", "C", "V", "B", "N", "M"])
        rows = [zero, one, two]
        print(zero)
        print(one)
        print(two)
        # iterate words
        ret_list = []
        # check each word
        for word in words:
            # check which set the first letter is in, assign to row var
            if len(word) > 0:
                if word[0].upper() in zero:
                    row = 0
                elif word[0].upper() in one:
                    row = 1
                else:
                    row = 2
            # iterate all letters and check if each letter is in the set (case sensitive)
            for i, letter in enumerate(word):
                if letter.upper() not in rows[row]:
                    break
                # if all letters in word are in one row, append to return list
                elif i == len(word) - 1:
                    ret_list.append(word)
                    
        # return list
        return ret_list