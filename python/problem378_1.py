from heapq import *


class Solution:
    def kthSmallest(self, matrix, k):
        r = len(matrix)
        c = len(matrix[0])
        hp = [(matrix[0][0], 0, 0)]
        for _ in range(k - 1):
            val, i, j = heappop(hp)
            if i == 0 and j < c - 1:
                heappush(hp, (matrix[i][j + 1], i, j + 1))
            if i < r - 1:
                heappush(hp, (matrix[i + 1][j], i + 1, j))
        return heappop(hp)[0]
