class Solution:
    def solveSudoku(self, board):
        self.solve(board)
        return board

    def solve(self, board):
        find = self.findEmpty(board)
        if not find:
            return True

        row, col = find
        for i in range(1, 10):
            if self.isValid(str(i), row, col, board):
                board[row][col] = str(i)
                if self.solve(board):
                    return True
                board[row][col] = "."
        return False

    def isValid(self, num, row, col, board):
        for c in range(9):
            if board[row][c] == num and c != col:
                return False
        for r in range(9):
            if board[r][col] == num and r != row:
                return False
        boxX = (row // 3) * 3
        boxY = (col // 3) * 3

        for rowidx in range(3):
            for colidx in range(3):
                curRow = boxX + rowidx
                curCol = boxY + colidx
                if board[curRow][curCol] == num:
                    return False

        return True

    def findEmpty(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    return i, j


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

Solution().solveSudoku(board)
