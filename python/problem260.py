from typing import Sequence


class Solution:
    def singleNumber(self, nums: Sequence[int]) -> Sequence[int]:
        axorb = 0
        for i in nums:
            axorb ^= i
        diff = axorb & -axorb
        a = 0
        for i in nums:
            if i & diff:
                a ^= i
        return [a, axorb ^ a]
