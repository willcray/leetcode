/*
https://leetcode.com/problems/perfect-squares/
time: O(N*log(N))
space: O(N)
Author: Will Cray
Date: 1/9/2020
*/

class Solution {
public:
    int numSquares(int n)
    {
        // solution 1: brute force
        // find perfect squares less than n
        // find all combinations of perfect squares less than n that sum to n
            // solve recursively
            // base case is current combination sums to n
                // if this combination is smaller than our smallest combination, update smallest combination
        // return num of numbers in smallest combination

        // solution 2: dynamic programming
        // iteratively build the results up to n
        // init count vector of size n + 1
        // count at 0 is 0, count at 1 is 1
        // recurrence condition
        // if current num isn't a perfect square, it
        // return result at index n

        // init vector full of n, because n is the highest possible number of perfect squares
        vector<int> count = vector<int>(n + 1, n);
        count.at(0) = 0;
        count.at(1) = 1;

        for (int i = 2; i <= n; ++i)
        {
            for (int j = 1; j * j <= i; ++j)
            {
                if (count.at(i) > (count.at(i - j * j) + 1))
                {
                    count.at(i) = count.at(i - j * j) + 1;
                }
            }
        }
        return count.at(n);
    }
};
