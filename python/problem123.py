from typing import Sequence


class Solution:
    def maxProfit(self, prices: Sequence[int]) -> int:
        if not prices:
            return 0
        buy1 = float('inf')
        sell1 = -float('inf')
        buy2 = float('inf')
        sell2 = -float('inf')
        for i in prices:
            buy1 = min(buy1, i)
            sell1 = max(sell1, i - buy1)
            buy2 = min(buy2, i - sell1)
            sell2 = max(sell2, i - buy2)
        return sell2
