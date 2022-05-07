from typing import Sequence


class Solution:
    def findDiagonalOrder(self, mat: Sequence[Sequence[int]]) -> Sequence[int]:
        x = 0
        y = 0
        r = len(mat)
        c = len(mat[0])
        res = [mat[0][0]]
        direction = True
        while not (x == r - 1 and y == c - 1):
            if direction:
                x -= 1
                y += 1
            else:
                x += 1
                y -= 1
            direction = not direction
            if y == c:
                y = c - 1
                x += 2
            elif x == r:
                x = r - 1
                y += 2
            elif y == -1:
                y = 0
            elif x == -1:
                x = 0
            else:
                direction = not direction
            res.append(mat[x][y])
        return res


if __name__ == '__main__':
    print(Solution().findDiagonalOrder(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
