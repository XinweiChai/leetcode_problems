from typing import Sequence


class Solution:
    def isCovered(self, ranges: Sequence[Sequence[int]], left: int, right: int) -> bool:
        ranges.sort()
        if ranges[0][0] > left:
            return False
        p = 0
        r = ranges[p][1]
        while p < len(ranges):
            if left < r and ranges[p][0] > r + 1:
                return False
            r = max(r, ranges[p][1])
            if r >= right:
                return True
            p += 1
        return False