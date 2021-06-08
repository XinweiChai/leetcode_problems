from typing import List

# First version: 3 iterations with complexity O(kn^2)
# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         if k == 0 or len(prices) < 2:
#             return 0
#         dp = [[0] * (k + 1) for _ in range(len(prices))]
#         for i in range(1, len(prices)):
#             for time in range(1, k + 1):
#                 temp = prices[0]
#                 for j in range(1, i):
#                     temp = min(temp, prices[j] - dp[j - 1][time - 1])
#                 dp[i][time] = max(dp[i - 1][time], prices[i] - temp)
#         return dp[-1][-1]
#
# First optimization:
# Remove i in the iteration of j then eliminate this iteration
# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         if k == 0 or len(prices) < 2:
#             return 0
#         dp = [[0] * (k + 1) for _ in range(len(prices))]
#         for time in range(1, k + 1):
#             temp = prices[0]
#             for i in range(1, len(prices)):
#                 temp = min(temp, prices[i] - dp[i - 1][time - 1])
#                 dp[i][time] = max(dp[i - 1][time], prices[i] - temp)
#         return dp[-1][-1]
#
# Second optimization: swap the loop of k and i
# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         if k == 0 or len(prices) < 2:
#             return 0
#         dp = [[0] * (k + 1) for _ in range(len(prices))]
#         temp = [prices[0]] * (k + 1)
#         for i in range(1, len(prices)):
#             for time in range(1, k + 1):
#                 temp[time] = min(temp[time], prices[i] - dp[i - 1][time - 1])
#                 dp[i][time] = max(dp[i - 1][time], prices[i] - temp[time])
#         return dp[-1][-1]


# Last optimization: iteration i only depends on i-1, this dimension in dp can be removed
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) < 2:
            return 0
        dp = [0] * (k + 1)
        temp = [prices[0]] * (k + 1)
        for i in range(1, len(prices)):
            for time in range(1, k + 1):
                temp[time] = min(temp[time], prices[i] - dp[time - 1])
                dp[time] = max(dp[time], prices[i] - temp[time])
        return dp[-1]


if __name__ == '__main__':
    print(Solution().maxProfit(k=2, prices=[2, 4, 1]))
