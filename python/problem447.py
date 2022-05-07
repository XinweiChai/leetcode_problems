from typing import Sequence


class Solution:
    def numberOfBoomerangs(self, points: Sequence[Sequence[int]]) -> int:
        cnt = 0
        for x1, y1 in points:
            lookup = {}
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                dx, dy = x1 - x2, y1 - y2
                d = dx * dx + dy * dy
                if d in lookup:
                    cnt += lookup[d]
                    lookup[d] += 1
                else:
                    lookup[d] = 1
        return 2 * cnt


if __name__ == '__main__':
    print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
