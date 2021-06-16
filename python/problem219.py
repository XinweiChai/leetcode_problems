from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for idx, i in enumerate(nums):
            if i in d and idx - d[i] <= k:
                return True
            d[i] = idx
        return False
