from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        tot = sum(wall[0])
        if tot == 1:
            return len(wall)
        c = {}
        for i in wall:
            cur = 0
            for j in i[:-1]:
                cur += j
                c[cur] = c.get(cur, 0) + 1
        return len(wall) - max(c.values(), default=0)


if __name__ == '__main__':
    print(Solution().leastBricks(wall=[[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))
