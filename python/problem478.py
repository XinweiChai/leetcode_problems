from typing import Sequence
import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> Sequence[float]:
        rad = random.random() * 2 * math.pi
        r = (self.r * random.random()) ** 0.5
        return [self.x + r * math.cos(rad), self.y + r * math.sin(rad)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()