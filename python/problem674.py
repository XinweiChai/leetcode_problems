from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 1
        anchor = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                anchor = i
            max_len = max(max_len, i - anchor + 1)
        return max_len
