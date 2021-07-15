import math
from functools import lru_cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        need = [[0] * (n + 1) for _ in range(n + 1)]
        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                need[lo][hi] = min(x + max(need[lo][x - 1], need[x + 1][hi])
                                   for x in range(lo, hi))
        return need[1][n]

    def getMoneyAmount2(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def rec(a, b):
            if b < 5:
                return [0, 0, 1, 2, 4][b]
            elif b == a + 2:
                return a + 1
            else:
                return min(i + max(rec(a, i - 1), rec(i + 1, b)) for i in range(b - 3, a, -4))
        return rec(1, n)


if __name__ == '__main__':
    print(Solution().getMoneyAmount2(5))
