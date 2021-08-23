from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        cnt = 0
        arrow = float('-inf')
        for begin, end in points:
            if begin > arrow:
                arrow = end
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
