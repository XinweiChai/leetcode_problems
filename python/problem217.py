from typing import Sequence


class Solution:
    def containsDuplicate(self, nums: Sequence[int]) -> bool:
        d = set()
        for i in nums:
            if i in d:
                return True
            d.add(i)
        return False
