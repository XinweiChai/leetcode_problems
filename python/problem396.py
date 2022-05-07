from typing import Sequence


class Solution:
    def maxRotateFunction(self, nums: Sequence[int]) -> int:
        ret = 0
        max_sum = float('-inf')
        for idx, i in enumerate(nums):
            ret += idx * i
        tot = sum(nums)
        for i in range(len(nums) - 1, -1, -1):
            ret += tot - nums[i] * len(nums)
            max_sum = max(max_sum, ret)
        return max_sum
