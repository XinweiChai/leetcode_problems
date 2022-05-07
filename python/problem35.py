from typing import Sequence


class Solution:
    def searchInsert(self, nums: Sequence[int], target: int) -> int:
        def rec(l, r):
            if l == r:
                return l
            mid = (l + r) // 2
            if target <= nums[mid]:
                return rec(l, mid)
            else:
                return rec(mid + 1, r)

        return rec(0, len(nums))


print(Solution().searchInsert([1, 3, 5, 6], 5))
