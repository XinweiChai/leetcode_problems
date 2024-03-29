from typing import Sequence


class Solution:
    def minPathSum(self, grid: Sequence[Sequence[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        for i in range(1, r):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, c):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
