from typing import List
import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.weight = []

        prefix = 0
        for i in w:
            prefix += i / total
            self.weight.append(prefix)

    def pickIndex(self) -> int:
        return bisect.bisect(self.weight, random.random())
