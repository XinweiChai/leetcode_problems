from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Timeout O(n^3)
        # cnt = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         if sum(nums[i:j]) == k:
        #             cnt += 1
        # return cnt

        # Kind of DP O(n^2)
        # cnt = 0
        # n = len(nums)
        # dp = []
        # for i in range(n + 1):
        #     dp.append(sum(nums[:i]))
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         if dp[j] - dp[i] == k:
        #             cnt += 1
        # return cnt

        # Without extra space O(n^2)
        # cnt = 0
        # n = len(nums)
        # for start in range(n):
        #     total = 0
        #     for end in range(start, n):
        #         total += nums[end]
        #         if total == k:
        #             cnt += 1
        # return cnt

        # Using Hashmap O(n)
        cnt = 0
        total = 0
        hm = {0: 1}
        n = len(nums)
        for i in range(n):
            total += nums[i]
            if total - k in hm:
                cnt += hm[total - k]
            hm[total] = hm[total] + 1 if total in hm else 1
        return cnt


print(Solution().subarraySum([1, 2, 3], 3))
