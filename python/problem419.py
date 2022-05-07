from typing import Sequence


class Solution:
    def countBattleships(self, board: Sequence[Sequence[str]]) -> int:
        r = len(board)
        c = len(board[0])
        cnt = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] != 'X') and (j == 0 or board[i][j - 1] != 'X'):
                    cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countBattleships(board=[["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
