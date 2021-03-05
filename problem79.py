class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r = len(board)
        c = len(board[0])

        # def rec(word, used, x, y):
        #     if not word:
        #         return True
        #     if x < r - 1 and (x + 1, y) not in used and word[0] == board[x + 1][y]:
        #         if rec(word[1:], used + [(x, y)], x + 1, y):
        #             return True
        #     if y < c - 1 and (x, y + 1) not in used and word[0] == board[x][y + 1]:
        #         if rec(word[1:], used + [(x, y)], x, y + 1):
        #             return True
        #     if x > 0 and (x - 1, y) not in used and word[0] == board[x - 1][y]:
        #         if rec(word[1:], used + [(x, y)], x - 1, y):
        #             return True
        #     if y > 0 and (x, y - 1) not in used and word[0] == board[x][y - 1]:
        #         if rec(word[1:], used + [(x, y)], x, y - 1):
        #             return True
        #     return False

        def rec(word, x, y):
            if not word:
                return True
            temp = board[x][y]
            board[x][y] = ''
            if x < r - 1 and word[0] == board[x + 1][y]:
                if rec(word[1:], x + 1, y):
                    return True
            if y < c - 1 and word[0] == board[x][y + 1]:
                if rec(word[1:], x, y + 1):
                    return True
            if x > 0 and word[0] == board[x - 1][y]:
                if rec(word[1:], x - 1, y):
                    return True
            if y > 0 and word[0] == board[x][y - 1]:
                if rec(word[1:], x, y - 1):
                    return True
            board[x][y] = temp
            return False

        def rec2(p, x, y):
            if p == len(word):
                return True
            temp = board[x][y]
            board[x][y] = ''
            if x < r - 1 and word[p] == board[x + 1][y] and rec2(p + 1, x + 1, y):
                return True
            if y < c - 1 and word[p] == board[x][y + 1] and rec2(p + 1, x, y + 1):
                return True
            if x > 0 and word[p] == board[x - 1][y] and rec2(p + 1, x - 1, y):
                return True
            if y > 0 and word[p] == board[x][y - 1] and rec2(p + 1, x, y - 1):
                return True
            board[x][y] = temp
            return False

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if rec2(1, i, j):
                        return True
        return False


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
