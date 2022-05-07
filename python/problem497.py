# Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.
import bisect
import random
from typing import Sequence
import itertools


class Solution:

    def __init__(self, rects: Sequence[Sequence[int]]):
        self.rects = rects
        self.area = [0] * len(rects)
        for i in range(len(rects)):
            a, b, x, y = rects[i]
            self.area[i] = (x - a + 1) * (y - b + 1)

    def pick(self) -> Sequence[int]:
        a, b, x, y = random.choices(self.rects, weights=self.area)[0]
        return [random.randint(a, x), random.randint(b, y)]


class Solution2:

    def __init__(self, rects: Sequence[Sequence[int]]):
        self.rects = rects
        pdf = []
        for x1, y1, x2, y2 in rects:
            pdf.append((x2 - x1 + 1) * (y2 - y1 + 1))
        self.cdf = list(itertools.accumulate(pdf))

    def pick(self) -> Sequence[int]:
        rand = int(random.random() * self.cdf[-1])
        i = bisect.bisect(self.cdf, rand)
        rand = self.cdf[i] - rand - 1
        x1, y1, x2, y2 = self.rects[i]

        q, r = divmod(rand, x2 - x1 + 1)
        return [x1 + r, y1 + q]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
