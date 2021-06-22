from itertools import combinations
from typing import List, Iterable


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[Iterable[int]]:
        # Using built-in functions
        # return [c for c in combinations(range(1, 10), k) if sum(c) == n]

        res = []

        def rec(k, n, last, cur):
            if k == 0:
                if n == 0:
                    res.append(cur)
            else:
                for i in range(last + 1, min(n, 9) + 1):
                    rec(k - 1, n - i, i, cur + [i])

        rec(k, n, 0, [])
        return res


if __name__ == '__main__':
    print(Solution().combinationSum3(k=3, n=7))
