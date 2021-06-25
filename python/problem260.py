from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        axorb = 0
        for i in nums:
            axorb ^= i
        diff = axorb & -axorb
        a = 0
        for i in nums:
            if i & diff:
                a ^= i
        return [a, axorb ^ a]
