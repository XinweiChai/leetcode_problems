from typing import Sequence


class Solution:
    def removeElement(self, nums: Sequence[int], val: int) -> int:
        r = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
        return r


print(Solution().removeElement([3, 2, 2, 3], 3))
