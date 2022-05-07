from typing import Sequence


class Solution:
    def numberOfArithmeticSlices(self, nums: Sequence[int]) -> int:
        tot = 0
        streak = 0
        for i in range(2, len(nums)):
            if nums[i - 2] + nums[i] == 2 * nums[i - 1]:
                streak += 1
            else:
                tot += streak * (streak + 1) // 2
                streak = 0
        tot += streak * (streak + 1) // 2
        return tot
