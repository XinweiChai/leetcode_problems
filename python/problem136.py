from typing import Sequence


class Solution:
    def singleNumber(self, nums: Sequence[int]) -> int:
        x = 0
        for i in nums:
            x ^= i
        return x
