from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set(nums)
        return (sum(s) * 3 - sum(nums)) // 2

        # Consider a generalization
        # "Given an array of integers, every element appears k (k > 1) times except for one,
        # which appears p times (p >= 1, p % k != 0). Find that single one."
