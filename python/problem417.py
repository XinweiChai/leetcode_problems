from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        pac = [[False] * c for _ in range(r)]
        atl = [[False] * c for _ in range(r)]
        new_pac = deque()
        new_atl = deque()
        for i in range(c):
            pac[0][i] = True
            new_pac.append((0, i))
            atl[r - 1][i] = True
            new_atl.append((r - 1, i))
        for i in range(r):
            pac[i][0] = True
            new_pac.append((i, 0))
            atl[i][c - 1] = True
            new_atl.append((i, c - 1))
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while new_pac:
            x, y = new_pac.popleft()
            for dx, dy in neighbors:
                if 0 <= x + dx < r and 0 <= y + dy < c and heights[x + dx][y + dy] >= heights[x][y] and not pac[x + dx][y + dy]:
                    pac[x + dx][y + dy] = True
                    new_pac.append((x + dx, y + dy))
        while new_atl:
            x, y = new_atl.popleft()
            for dx, dy in neighbors:
                if 0 <= x + dx < r and 0 <= y + dy < c and heights[x + dx][y + dy] >= heights[x][y] and not atl[x + dx][y + dy]:
                    atl[x + dx][y + dy] = True
                    new_atl.append((x + dx, y + dy))

        ret = []
        for i in range(r):
            for j in range(c):
                if pac[i][j] == 1 and atl[i][j] == 1:
                    ret.append([i, j])
        return ret


if __name__ == '__main__':
    print(Solution().pacificAtlantic(
        [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
