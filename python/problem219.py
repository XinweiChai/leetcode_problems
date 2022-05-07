from typing import Sequence


class Solution:
    def containsNearbyDuplicate(self, nums: Sequence[int], k: int) -> bool:
        d = {}
        for idx, i in enumerate(nums):
            if i in d and idx - d[i] <= k:
                return True
            d[i] = idx
        return False
