class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        queens = []
        cols = [True] * n

        def dfs(row):
            nonlocal res
            if len(queens) == n:
                res +=1
            for i in range(n):
                if cols[i]:
                    diag = True
                    for r, c in queens:
                        if row - i == r - c or row + i == r + c:
                            diag = False
                            break
                    if diag:
                        cols[i] = False
                        queens.append((row, i))
                        dfs(row + 1)
                        queens.pop()
                        cols[i] = True

        dfs(0)
        return res
