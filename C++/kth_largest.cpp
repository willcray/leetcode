/*
https://leetcode.com/problems/kth-largest-element-in-an-array/
time: O(N*log(N))
space: O(1)
Author: Will Cray
Date: 1/8/2020
*/


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k)
    {

        // check for array of size zero
        if (nums.size() == 0)
        {
            return 0;
        }
        /*
        // solution 1 - sort array and return the kth largest element
        // time - O(N*log(N)), where N is nums.size()
        // space - O(1) if we sort in place
        sort(nums.begin(), nums.end());

        return nums.at(nums.size() - k);
        */

        // solution 2 - iterate the vector k times and remove the greatest element each time
        // return the removed element on the kth iteration
        // time - O(N^3)
        // space - O(1)

        // solution 3 - priority queue/min heap
        // time - O(N * log(N))
        // space - O(k)
        priority_queue <int, vector<int>, greater<int>> pq;

        for (int num : nums)
        {
            pq.push(num);
            if (pq.size() > k)
            {
                pq.pop();
            }
        }
        return pq.top();
    }
};
