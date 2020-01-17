"""
https://leetcode.com/problems/shuffle-an-array/
time: O(N)
space: O(1)
Author: Will Cray
Date: 1/14/2020
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ans = self.nums[:]

        for i in range(len(ans) - 1, 0, -1):
            j = random.randint(0, i)
            ans[i], ans[j] = ans[j], ans[i]

        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
