import collections
from typing import Sequence


class Solution:
    def gameOfLife(self, board: Sequence[Sequence[int]]):
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len((board[0]))
        neighbors = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        for i in range(r):
            for j in range(c):
                board[i][j] *= 3
        for i in range(r):
            for j in range(c):
                live_neighbors = 0
                for k in neighbors:
                    row = i + k[0]
                    col = j + k[1]
                    if (0 <= row < r) and (0 <= col < c) and board[row][col] & 2:
                        live_neighbors += 1
                if not board[i][j] & 2 and live_neighbors == 3:
                    board[i][j] |= 1
                if board[i][j] & 2 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] &= (~1)
        for i in range(r):
            for j in range(c):
                board[i][j] &= 1

    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J)
                                  for i, j in live
                                  for I in range(i - 1, i + 2)
                                  for J in range(j - 1, j + 2)
                                  if I != i or J != j)
        return {ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

    def gameOfLifeInf(self, board):
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)

# print(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
print(Solution().gameOfLifeInf([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
