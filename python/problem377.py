from functools import lru_cache
from typing import Sequence


class Solution:
    # def combinationSum4(self, nums: Sequence[int], target: int) -> int:
    #     @lru_cache
    #     def rec(target):
    #         if target == 0:
    #             return 1
    #         elif target < 0:
    #             return 0
    #         else:
    #             return sum(rec(target - i) for i in nums)
    #     return rec(target)

    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * target
        for i in range(target + 1):
            for num in nums:
                if num > i: break
                if num == i: combs[i] += 1
                if num < i: combs[i] += combs[i - num]
        return combs[target]


if __name__ == '__main__':
    print(Solution().combinationSum4([1, 2, 3], 4))
