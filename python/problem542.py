from typing import List
import collections


class Solution:
    # BFS
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        def adj(x, y):
            d = ((0, 1), (1, 0), (-1, 0), (0, -1))
            return [(x + dx, y + dy) for dx, dy in d if 0 <= x + dx < row and 0 <= y + dy < col]

        done = collections.deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1 and any(mat[x][y] == 0 for x, y in adj(i, j)):
                    done.append((i, j))
                    mat[i][j] = -1
        cnt = 2
        cp = list(done)
        while done:
            c = len(done)
            for _ in range(c):
                i, j = done.popleft()
                for x, y in adj(i, j):
                    if mat[x][y] == 1:
                        mat[x][y] = cnt
                        done.append((x, y))
            cnt += 1
        for i, j in cp:
            mat[i][j] = 1
        return mat

    # Update from two directions, guaranteeing the value is less than or equal to its neighbor + 1
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        dist = [[float('inf') if mat[i][j] == 1 else 0 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                if i < r - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j < c - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist


if __name__ == '__main__':
    print(
        Solution().updateMatrix2([[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]))
