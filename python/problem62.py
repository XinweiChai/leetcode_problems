class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype -> int
        """
        board = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i - 1][j] + board[i][j - 1]
        return board[m - 1][n - 1]


print(Solution().uniquePaths(1, 1))
