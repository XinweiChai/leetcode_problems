from typing import List
import random


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.tot = m * n
        self.map = {}

    # In each flip, the random choice is linked with the last cell,
    # which will be never chosen afterwards,
    # in case we step on duplicate, use its linked cell and update the link with current last one.
    def flip(self) -> List[int]:
        self.tot -= 1
        r = random.randint(0, self.tot)
        x = self.map.get(r, r)
        self.map[r] = self.map.get(self.tot, self.tot)
        return divmod(x, self.n)

    def reset(self) -> None:
        self.tot = self.m * self.n
        self.map.clear()


# Your Solution object will be instantiated and called as such:
obj = Solution(1000, 1000)
print(obj.flip())
print(obj.flip())
print(obj.flip())
print(obj.flip())
print(obj.flip())
print(obj.flip())
obj.reset()
x = 1
