from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def check(x1, y1, x2, y2):
            val = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] != val:
                        return 2
            return val

        def rec(x1, y1, x2, y2):
            val = check(x1, y1, x2, y2)
            if val == 2:
                midx = (x1 + x2) // 2
                midy = (y1 + y2) // 2
                return Node(val, False, rec(x1, y1, midx, midy), rec(x1, midy, midx, y2), rec(midx, y1, x2, midy),
                            rec(midx, midy, x2, y2))
            else:
                return Node(val, True, None, None, None, None)

        return rec(0, 0, n, n)


if __name__ == '__main__':
    x = Solution().construct([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])
    y=1
