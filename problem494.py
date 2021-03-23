from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # O(n*2^n)
        # n = len(nums)
        # cnt = 0
        # for i in range(2 ** n, 2 ** (n + 1)):
        #     bitmask = bin(i)[3:]
        #     total = 0
        #     for j in range(n):
        #         if bitmask[j] == '1':
        #             total -= int(nums[j])
        #         else:
        #             total += int(nums[j])
        #     if total == S:
        #         cnt += 1
        # return cnt

        



print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 5))
