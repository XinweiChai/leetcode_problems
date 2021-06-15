from typing import List


def removeBrick(board: List[List[int]], x: int, y: int):
    if board[x][y] == 0:
        return board
    r = len(board)
    c = len(board[0])
    board[x][y] = 0

    def neighbors(x, y):
        ans = set()
        dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for i in dxdy:
            if 0 <= x + i[0] < r and 0 <= y + i[1] < c and board[x + i[0]][y + i[1]] == 1:
                ans.add((x + i[0], y + i[1]))
        return ans

    def stable(x, y):
        dx = dy = [-1, 1]
        xneighbor = [[x + i, y] for i in dx if 0 <= x + i < r]
        yneighbor = [[x, y + i] for i in dy if 0 <= y + i < c]
        res1 = True
        for i in xneighbor:
            if board[i[0]][i[1]] == 0:
                res1 = False
        res2 = True
        for i in yneighbor:
            if board[i[0]][i[1]] == 0:
                res2 = False
        return res1 or res2

    flip = True
    bricks = neighbors(x, y)
    while flip:
        flip = False
        temp = set()
        for i in list(bricks):
            if not stable(i[0], i[1]):
                flip = True
                board[i[0]][i[1]] = 0
                bricks.remove((i[0], i[1]))
                temp.union(neighbors(i[0], i[1]))
                bricks = temp
    return board
