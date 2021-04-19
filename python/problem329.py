from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        r = len(matrix)
        c = len(matrix[0])
        table = {}

        def dfs(i, j):
            if (i, j) in table:
                return table[(i, j)]
            res = 1
            for k in neighbors:
                row = i + k[0]
                col = j + k[1]
                if 0 <= row < r and 0 <= col < c and matrix[row][col] > matrix[i][j]:
                    res = max(res, dfs(row, col) + 1)
            table[(i, j)] = res
            return res

        max_path = 0
        for i in range(r):
            for j in range(c):
                max_path = max(max_path,dfs(i, j))
        return max_path


print(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
