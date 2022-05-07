from typing import Sequence


class Solution:
    def isRectangleCover(self, rectangles: Sequence[Sequence[int]]) -> bool:
        x1 = float('inf')
        x2 = float('-inf')
        y1 = float('inf')
        y2 = float('-inf')

        s = set()
        area = 0
        for i in rectangles:
            x1 = min(x1, i[0])
            y1 = min(y1, i[1])
            x2 = max(x2, i[2])
            y2 = max(y2, i[3])
            area += (i[2] - i[0]) * (i[3] - i[1])

            s1 = (i[0], i[1])
            s2 = (i[0], i[3])
            s3 = (i[2], i[3])
            s4 = (i[2], i[1])

            s.remove(s1) if s1 in s else s.add(s1)
            s.remove(s2) if s2 in s else s.add(s2)
            s.remove(s3) if s3 in s else s.add(s3)
            s.remove(s4) if s4 in s else s.add(s4)

        if (x1, y1) not in s or (x1, y2) not in s or (x2, y1) not in s or (x2, y2) not in s or len(s) != 4:
            return False
        return area == (x2 - x1) * (y2 - y1)

    def isRectangleCover2(self, rectangles: Sequence[Sequence[int]]) -> bool:
        points = set()
        area = 0
        for rect in rectangles:
            x, y, a, b = rect
            for p in [(x, y), (x, b), (a, y), (a, b)]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
            area += (a - x) * (b - y)
        cp = sorted(list(points), key=lambda x: (x[0], x[1]))  # corner point
        return len(points) == 4 and (area == (cp[-1][0] - cp[0][0]) * (cp[-1][1] - cp[0][1]))


if __name__ == '__main__':
    print(Solution().isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]))
