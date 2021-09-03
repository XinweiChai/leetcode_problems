from collections import defaultdict


class Solution:
    # Faster backtrack version
    def solveSudoku(self, board):
        rows, cols, triples, visit = defaultdict(set), defaultdict(set), defaultdict(set), []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[r // 3, c // 3].add(board[r][c])
                else:
                    visit.append((r, c))

        def dfs():
            if not visit:
                return True
            r, c = visit[-1]
            t = (r // 3, c // 3)
            for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                    board[r][c] = dig
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    visit.pop()
                    if dfs():
                        return True
                    else:
                        board[r][c] = "."
                        rows[r].discard(dig)
                        cols[c].discard(dig)
                        triples[t].discard(dig)
                        visit.append((r, c))
            return False

        dfs()


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

Solution().solveSudoku(board)
