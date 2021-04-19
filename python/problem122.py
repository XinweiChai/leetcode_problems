from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        while buy < len(prices) - 1:
            if prices[buy] < prices[buy + 1]:
                profit += prices[buy + 1] - prices[buy]
            buy += 1
        return profit
