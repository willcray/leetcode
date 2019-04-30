"""
https://leetcode.com/problems/valid-palindrome/
Author: Will Cray
Date: 4/30/2019
Time: O(n)
Space: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # note: ignoring cases
        # only considering alphanumeric strings (A-Z, 0-9)
        # check if empty string
        # if only one characters, it's a palindrome
    
        l, r = 0, len(s) - 1
        while r > l:
            
            # while r > l and l is not alphanumeric
            while r > l and not s[l].isalnum():
                l += 1
            
            # while r > land r is not alphanumeric
            while r > l and not s[r].isalnum():
                r -= 1
                
            # if s[r] is not equal to s[l], ensuring consistent cases
            if s[r].lower() != s[l].lower(): 
                return False
            
            else:
                # iterate r and l
                r -= 1
                l += 1
        
        # reached the middle without finding a difference        
        return True