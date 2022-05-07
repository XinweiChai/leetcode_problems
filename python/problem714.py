from typing import Sequence


class Solution:
    def maxProfit(self, prices: Sequence[int], fee: int) -> int:
        not_hold = 0
        hold = -prices[0] - fee
        for i in range(1, len(prices)):
            hold = max(hold, not_hold - prices[i] - fee)
            not_hold = max(not_hold, prices[i] + hold)
        return not_hold


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
