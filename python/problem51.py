from typing import Sequence


class Solution:
    def solveNQueens(self, n: int) -> Sequence[Sequence[str]]:
        res = []
        queens = []
        cols = [True] * n

        def dfs(row):
            if len(queens) == n:
                board = [['.'] * n for _ in range(n)]
                for i, j in queens:
                    board[i][j] = 'Q'
                board = ["".join(i) for i in board]
                res.append(board)
            for i in range(n):
                if cols[i]:
                    diag = True
                    for r, c in queens:
                        if row - i == r - c or row + i == r + c:
                            diag = False
                            break
                    if diag:
                        cols[i] = False
                        queens.append((row, i))
                        dfs(row + 1)
                        queens.pop()
                        cols[i] = True

        dfs(0)
        return res


print(len(Solution().solveNQueens(8)))
