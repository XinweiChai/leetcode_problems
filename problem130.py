class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])

        to_keep = []
        for i in range(c):
            if board[0][i] == 'O':
                board[0][i] = 'S'
                to_keep.append((0, i))
            if board[r - 1][i] == 'O':
                board[r - 1][i] = 'S'
                to_keep.append((r - 1, i))
        for i in range(1, r - 1):
            if board[i][0] == 'O':
                board[i][0] = 'S'
                to_keep.append((i, 0))
            if board[i][c - 1] == 'O':
                board[i][c - 1] = 'S'
                to_keep.append((i, c - 1))

        while to_keep:
            row, col = to_keep.pop()
            if row + 1 < r and board[row + 1][col] == 'O':
                board[row + 1][col] = 'S'
                to_keep.append((row + 1, col))
            if col + 1 < c and board[row][col + 1] == 'O':
                board[row][col + 1] = 'S'
                to_keep.append((row, col + 1))
            if row - 1 >= 0 and board[row - 1][col] == 'O':
                board[row - 1][col] = 'S'
                to_keep.append((row - 1, col))
            if col - 1 >= 0 and board[row][col - 1] == 'O':
                board[row][col - 1] = 'S'
                to_keep.append((row, col - 1))
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

# print(Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
