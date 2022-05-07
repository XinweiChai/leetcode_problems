import itertools
from functools import lru_cache
from itertools import starmap
from typing import Sequence


class Solution:
    def longestIncreasingPath(self, matrix: Sequence[Sequence[int]]) -> int:
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        r = len(matrix)
        c = len(matrix[0])
        table = {}

        def dfs(i, j):
            if (i, j) in table:
                return table[i, j]
            res = 1
            for k in neighbors:
                row = i + k[0]
                col = j + k[1]
                if 0 <= row < r and 0 <= col < c and matrix[row][col] > matrix[i][j]:
                    res = max(res, dfs(row, col) + 1)
            table[i, j] = res
            return res

        max_path = 0
        for i in range(r):
            for j in range(c):
                max_path = max(max_path, dfs(i, j))
        return max_path

    # dfs + cache
    def longestIncreasingPath2(self, matrix: Sequence[Sequence[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def max_d(r, c):
            val = matrix[r][c]
            return 1 + max(
                max_d(r + 1, c) if r < m - 1 and val > matrix[r + 1][c] else 0,
                max_d(r - 1, c) if r > 0 and val > matrix[r - 1][c] else 0,
                max_d(r, c + 1) if c < n - 1 and val > matrix[r][c + 1] else 0,
                max_d(r, c - 1) if c > 0 and val > matrix[r][c - 1] else 0)

        return max(starmap(max_d, itertools.product(range(m), range(n))))


if __name__ == '__main__':
    print(Solution().longestIncreasingPath2([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
