from typing import Sequence


class Solution:
    def maxProfit(self, prices: Sequence[int]) -> int:
        maxCur = 0
        maxSoFar = 0
        for i in range(1,len(prices)):
            maxCur = max(0, maxCur + prices[i] - prices[i-1])
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
