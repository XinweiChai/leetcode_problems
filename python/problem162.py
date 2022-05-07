from typing import Sequence


class Solution:
    def findPeakElement(self, nums: Sequence[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


print(Solution().findPeakElement([3, 1, 2]))
