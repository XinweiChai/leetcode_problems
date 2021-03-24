from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # O(2^n)
        # cnt = 0
        #
        # def trial(p, s):
        #     nonlocal cnt
        #     if p == len(nums):
        #         if s == 0:
        #             cnt += 1
        #     else:
        #         trial(p + 1, s + nums[p])
        #         trial(p + 1, s - nums[p])
        #
        # trial(0, S)
        # return cnt

        # Memoization
        return self.trial(0, nums, S)

    def trial(self,p,nums, s):
        if (p, s) in self.memo:
            return self.memo[(p, s)]
        if p == len(nums):
            if s == 0:
                return 1
            else:
                return 0
        else:
            pos = self.trial(p + 1, nums,s + nums[p])
            neg = self.trial(p + 1, nums,s - nums[p])
            self.memo[(p, s)] = pos + neg
            return self.memo[(p, s)]



print(Solution().findTargetSumWays([11, 19, 14, 50, 47, 35, 18, 32, 8, 2, 31, 45, 6, 25, 49, 23, 25, 33, 24, 33], 44))
print(Solution().findTargetSumWays([1], 1))
