from typing import List
import operator


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    cnt += 4
                    adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    for dx, dy in adj:
                        if 0 <= i + dx < r and 0 <= j + dy < c and grid[i + dx][j + dy]:
                            cnt -= 1
        return cnt

    # WTF
    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
                   for row in grid + list(map(list, zip(*grid))))


if __name__ == '__main__':
    print(Solution().islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
