from typing import Sequence


class Solution:
    def generateMatrix(self, n: int) -> Sequence[Sequence[int]]:
        if n == 1:
            return [[1]]
        res = [[0] * n for _ in range(n)]
        dl = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cnt = 0
        r, c = 0, 0
        for i in range(n * n):
            res[r][c] = i + 1
            dr, dc = dl[cnt % 4]
            r += dr
            c += dc
            if (dr == 1 and (r == n - 1 or res[r + 1][c])) or \
                    (dr == -1 and (r == 0 or res[r - 1][c])) or \
                    (dc == 1 and (c == n - 1 or res[r][c + 1])) or \
                    (dc == -1 and (c == 0 or res[r][c - 1])):
                cnt += 1
        return res


print(Solution().generateMatrix(1))
