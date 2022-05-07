from functools import lru_cache
from typing import Sequence


class Solution:
    def PredictTheWinner(self, nums: Sequence[int]) -> bool:
        @lru_cache
        def p1(left, right):
            if left == right:
                return nums[left]
            return max(p2(left + 1, right) + nums[left], p2(left, right - 1) + nums[right])

        @lru_cache
        def p2(left, right):
            if left == right:
                return nums[left]
            return min(p1(left + 1, right), p1(left, right - 1))

        res = p1(0, len(nums) - 1)
        return res * 2 >= sum(nums)

    def PredictTheWinner2(self, nums: Sequence[int]) -> bool:
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for s in range(len(nums) - 1, -1, -1):
            for e in range(s, len(nums)):
                if s == e:
                    dp[s][e] = nums[e]
                else:
                    dp[s][e] = max(nums[e] - dp[s][e - 1], nums[s] - dp[s + 1][e])
        return dp[0][-1] >= 0

    def PredictTheWinner3(self, nums: Sequence[int]) -> bool:
        dp = [0] * len(nums)
        for s in range(len(nums) - 1, -1, -1):
            for e in range(s, len(nums)):
                if s == e:
                    dp[s] = nums[e]
                else:
                    dp[e] = max(nums[e] - dp[e - 1], nums[s] - dp[e])
        return dp[-1] >= 0


if __name__ == '__main__':
    print(Solution().PredictTheWinner3([1, 5, 2]))
