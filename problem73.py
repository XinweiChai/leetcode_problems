from typing import List


class Solution(object):
    def setZeroes(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        # pos = []
        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j] == 0:
        #             pos.append((i, j))
        # for k in pos:
        #     matrix[k[0]] = [0] * c
        #     for i in range(r):
        #         matrix[i][k[1]] = 0

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    for m in range(c):
                        if matrix[i][m] != 0:
                            matrix[i][m] = None
                    for n in range(r):
                        if matrix[n][j] != 0:
                            matrix[n][j] = None
        for i in range(r):
            for j in range(c):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
        return matrix

print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
