from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r = len(board)
        c = len(board[0])
        cr, cc = click

        def adjacent(x, y):
            d = [1, 0, -1]
            return [(x + dx, y + dy) for dx in d for dy in d if
                    0 <= x + dx < r and 0 <= y + dy < c and not dx == dy == 0]

        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
        else:
            temp = sum(board[i][j] != 'M' for i, j in adjacent(cr, cc))
            if temp == 0:
                board[cr][cc] = 'B'
                for i, j in adjacent(cr, cc):
                    if board[i][j] == 'E':
                        self.updateBoard(board, [i, j])
            else:
                board[cr][cc] = str(temp)
        return board


if __name__ == '__main__':
    print(Solution().updateBoard(board=[["E", "E", "E", "E", "E"],
                                        ["E", "E", "M", "E", "E"],
                                        ["E", "E", "E", "E", "E"],
                                        ["E", "E", "E", "E", "E"]], click=[0, 0]))
