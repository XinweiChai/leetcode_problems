from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        for i in range(len(nums)):
            nums[(nums[i] - 1) % len(nums)] += len(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] < len(nums) + 1:
                res.append(i + 1)
        return res


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
