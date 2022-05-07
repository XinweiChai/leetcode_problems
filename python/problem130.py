from typing import Sequence


class Solution:
    def solve(self, board: Sequence[Sequence[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        to_keep = []
        for i in range(c):
            for j in (0, r - 1):
                if board[j][i] == 'O':
                    board[j][i] = 'S'
                    to_keep.append((j, i))
        for i in range(1, r - 1):
            for j in (0, c - 1):
                if board[i][j] == 'O':
                    board[i][j] = 'S'
                    to_keep.append((i, j))

        adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while to_keep:
            row, col = to_keep.pop()
            for i, j in adjacent:
                if 0 <= row + i < r and 0 <= col + j < c and board[row + i][col + j] == 'O':
                    board[row + i][col + j] = 'S'
                    to_keep.append((row + i, col + j))
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
        return board
        # flip = [[True] * c for _ in range(r)]
        # visited = [[False] * c for _ in range(r)]
        #
        # def rec(row, col):
        #     if 0 <= row <= r - 1 and 0 <= col <= c - 1 and board[row][col] == 'O' and not visited[row][col]:
        #         visited[row][col] = True
        #         if not flip[row][col]:
        #             if row < r - 1:
        #                 flip[row + 1][col] = False
        #             if col < c - 1:
        #                 flip[row][col + 1] = False
        #             if row > 0:
        #                 flip[row - 1][col] = False
        #             if col > 0:
        #                 flip[row][col - 1] = False
        #         rec(row + 1, col)
        #         rec(row, col + 1)
        #         rec(row - 1, col)
        #         rec(row, col - 1)
        #
        # for i in range(c):
        #     flip[0][i] = False
        #     flip[r - 1][i] = False
        #     rec(0, i)
        #     rec(r - 1, i)
        # for i in range(1, r - 1):
        #     flip[i][0] = False
        #     flip[i][c - 1] = False
        #     rec(i, 0)
        #     rec(i, c - 1)
        # for i in range(r):
        #     for j in range(c):
        #         if board[i][j] == 'O' and flip[i][j]:
        #             board[i][j] = 'X'
        # return board


print(Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
