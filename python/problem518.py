from functools import lru_cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()

        @lru_cache(maxsize=None)
        def helper(rest, lmt):
            if rest == 0:
                return 1
            cnt = 0
            for i in range(lmt, -1, -1):
                if coins[i] <= rest:
                    cnt += helper(rest - coins[i], i)
            return cnt

        return helper(amount, n - 1)

    # Clever solution
    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(amount - coin + 1):
                if dp[i]:
                    dp[i + coin] += dp[i]
        return dp[amount]


if __name__ == '__main__':
    print(Solution().change2(amount=500, coins=[1, 2, 5]))
