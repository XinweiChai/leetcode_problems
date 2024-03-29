from typing import Sequence


class Solution:
    def maxProfit(self, prices: Sequence[int]) -> int:
        buy = 0
        profit = 0
        while buy < len(prices) - 1:
            if prices[buy] < prices[buy + 1]:
                profit += prices[buy + 1] - prices[buy]
            buy += 1
        return profit
