from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Using O(n) space
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        board = [0] * (n + 1)
        board[1] = 1
        for i in range(m):
            for j in range(1, n + 1):
                if obstacleGrid[i][j - 1] != 1:
                    board[j] += board[j - 1]
                else:
                    board[j] = 0
        return board[n]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
