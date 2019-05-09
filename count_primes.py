"""
https://leetcode.com/problems/count-primes/
Author: Will Cray
Date: 5/8/2019
Time: O(N)
Space: O(N)
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """        
        if n <= 2:
            return 0
        
        primes = [1] * n
        
        primes[0] = 0
        primes[1] = 0
        
        for i in range(2, int(n**0.5) + 1):
            # we've already marked it as non-prime if it's zero
            if primes[i] != 0:
                # mark all multiples of itself as non-prime
                for j in range(i*i, n, i):
                    primes[j] = 0
        return sum(primes)