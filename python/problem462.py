from typing import Sequence


class Solution:
    def minMoves2(self, nums: Sequence[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(i - median) for i in nums)
