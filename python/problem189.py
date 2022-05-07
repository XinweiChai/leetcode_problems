from typing import Sequence


class Solution:
    def rotate(self, nums: Sequence[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        def rev(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        rev(0, len(nums) - 1)
        rev(0, k - 1)
        rev(k, len(nums) - 1)
