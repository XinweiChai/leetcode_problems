from typing import Sequence


class Solution:
    def findWords(self, board: Sequence[Sequence[str]], words: Sequence[str]) -> Sequence[str]:
        coord = {}
        for i in range(ord('a'), ord('z') + 1):
            coord[chr(i)] = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                coord[board[i][j]].append((i, j))

        def is_adjacent(a, b):
            if a[0] == b[0]:
                return a[1] == b[1] + 1 or a[1] == b[1] - 1
            if a[1] == b[1]:
                return a[0] == b[0] + 1 or a[0] == b[0] - 1

        def dfs(word, char, used_coord):
            if char == len(word):
                return True
            for i in coord[word[char]]:
                if char == 0 or (is_adjacent(used_coord[-1], i) and i not in used_coord):
                    if dfs(word, char + 1, used_coord + [i]):
                        return True
            return False

        ans = []
        for i in words:
            if dfs(i, 0, []):
                ans.append(i)
        return ans


print(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                           ["oath", "pea", "eat", "rain"]))
