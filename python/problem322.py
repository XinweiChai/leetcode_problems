from typing import Sequence


class Solution:
    def coinChange(self, coins: Sequence[int], amount: int) -> int:
        # recursion with dp, costing a lot of memory
        # if amount == 0:
        #     return 0
        # table = {}
        # coins.sort(reverse=True)
        #
        # def dp(money):
        #     if money in table:
        #         return table[money]
        #     if money in coins:
        #         return 1
        #     min_coins = float('inf')
        #     for i in coins:
        #         if i < money:
        #             temp = dp(money - i)
        #             if temp == 1:
        #                 min_coins = 2
        #                 break
        #             if temp<min_coins:
        #                 min_coins = temp + 1
        #     table[money] = min_coins
        #     return min_coins
        # res = dp(amount)
        # if res == float('inf'):
        #     return -1
        # return res

        # DP
        table = {0: 0}
        coins.sort(reverse=True)
        for i in range(1, amount + 1):
            table[i] = min([table[i - j] for j in coins if j <= i and (i - j) in table]+[float('inf')]) + 1
        if table[amount] == float('inf'):
            return -1
        else:
            return table[amount]


print(Solution().coinChange([1, 2, 5], 11))
