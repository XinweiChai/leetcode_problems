from typing import Sequence


class Solution:
    # Similar to solution LC188
    #
    def maxProfit(self, prices: Sequence[int]) -> int:
        dp = [0] * (len(prices) + 2)
        max_val = -prices[0]
        for i in range(1, len(prices)):
            max_val = max(max_val, dp[i] - prices[i])
            dp[i + 2] = max(max_val + prices[i], dp[i + 1])
        return dp[-1]

    # Using O(1) space
    def maxProfit2(self, prices: Sequence[int]) -> int:
        two_day_bef = one_day_bef = cur = 0
        max_val = -prices[0]
        for i in range(1, len(prices)):
            max_val = max(max_val, two_day_bef - prices[i])
            cur = max(max_val + prices[i], one_day_bef)
            two_day_bef, one_day_bef, = one_day_bef, cur

        return cur

    # Using one less variable
    def maxProfit3(self, prices: Sequence[int]) -> int:
        temp = cur = 0
        max_val = -prices[0]
        for i in range(1, len(prices)):
            max_val = max(max_val, temp - prices[i])
            temp = cur
            cur = max(max_val + prices[i], cur)

        return cur

    # WTF
    def maxProfit4(self, prices: Sequence[int]) -> int:
        free = 0
        have = cool = float('-inf')
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
        return max(free, cool)


if __name__ == '__main__':
    print(Solution().maxProfit3(prices=[1, 2, 3, 0, 2]))
