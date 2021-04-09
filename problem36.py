from typing import List


class Solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = len(board)
        for i in range(r):
            row = [True] * r
            col = [True] * r
            for j in range(r):
                if board[i][j] != '.':
                    if row[int(board[i][j]) - 1]:
                        row[int(board[i][j]) - 1] = False
                    else:
                        return False
                if board[j][i] != '.':
                    if col[int(board[j][i]) - 1]:
                        col[int(board[j][i]) - 1] = False
                    else:
                        return False
        for k in range(r):
            box = [True] * r
            for i in range((k // 3) * 3, (k // 3) * 3 + 3):
                for j in range((k % 3 * 3), (k % 3 * 3) + 3):
                    if board[i][j] != '.':
                        if box[int(board[i][j]) - 1]:
                            box[int(board[i][j]) - 1] = False
                        else:
                            return False
        return True
