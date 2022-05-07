from typing import Sequence


class Solution:
    def maxSubArray(self, nums: Sequence[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
