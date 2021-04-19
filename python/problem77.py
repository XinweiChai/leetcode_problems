from typing import List
import itertools


class Solution:
    def combine(self, n: int, k: int):
        # Built-in function
        # return itertools.combinations(range(1, n + 1), k)
        if k == 0:
            return [[]]
        return [j + [i] for i in range(k, n + 1) for j in self.combine(i - 1, k - 1)]


print(Solution().combine(4, 2))
