from typing import List


class Solution(object):
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        p = 0
        begin = 1
        while nums[p] + p < len(nums) - 1:
            long_dist = 0
            i = 0
            for i in range(begin, nums[p] + p + 1):
                if i + nums[i] >= long_dist:
                    p = i
                    long_dist = i + nums[i]
            if nums[p] == 0:
                return False
            begin = i + 1
        return True


# print(Solution().canJump([3, 2, 1, 0, 4]))
print(Solution().canJump([0, 1]))
