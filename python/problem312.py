from typing import List


class Solution:

    # Maximum recursion
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [i for i in nums if i != 0] + [1]
        n = len(nums)
        memo = {}

        def dp(left, right):
            if left > right:
                return 0
            if (left, right) not in memo:
                memo[(left, right)] = max(dp(left, i - 1) + dp(i + 1, right) +
                                          nums[left - 1] * nums[i] * nums[right + 1]
                                          for i in range(left, right + 1))
            return memo[(left, right)]

        return dp(1, n - 2)

    def maxCoins2(self, nums: List[int]) -> int:
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for l in range(0, n - k):
                r = l + k
                for i in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], nums[l] * nums[i] * nums[r] + dp[l][i] + dp[i][r])
        return dp[0][n - 1]


if __name__ == '__main__':
    print(Solution().maxCoins2([3, 1, 5, 8]))
