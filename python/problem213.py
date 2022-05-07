from typing import Sequence


class Solution:
    def rob(self, nums: Sequence[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def max_rob(new_nums):
            cur = last = 0
            for i in new_nums:
                last, cur = cur, max(last + i, cur)
            return cur

        return max(max_rob(nums[:-1]), max_rob(nums[1:]))


print(Solution().rob([2, 3, 2]))
