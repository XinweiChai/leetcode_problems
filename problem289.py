class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
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


print(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
