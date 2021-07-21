from functools import lru_cache
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        res = self.bt(stones, 1, 1, target)
        return res

    def bt(self, stones, cur, speed, target):
        # check memo
        if (cur, speed) in self.memo:
            return False

        if cur == target:
            return True

        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False
        # dfs
        candidate = [speed - 1, speed, speed + 1]
        for c in candidate:
            if (cur + c) in stones:
                if self.bt(stones, cur + c, c, target):
                    return True

        self.memo.add((cur, speed))
        return False

    def canCross2(self, stones: List[int]) -> bool:
        dict_stones = {i: idx for idx, i in enumerate(stones)}
        steps = [set() for _ in range(len(stones))]
        steps[0].add(0)
        for idx, i in enumerate(stones):
            for j in steps[idx]:
                if i + j in dict_stones:
                    steps[dict_stones[i + j]].add(j)
                if j > 1 and i + j - 1 in dict_stones:
                    steps[dict_stones[i + j - 1]].add(j - 1)
                if i + j + 1 in dict_stones:
                    steps[dict_stones[i + j + 1]].add(j + 1)
        return bool(steps[-1])


if __name__ == '__main__':
    print(Solution().canCross2([0, 1,2,3,4,5]))
