from typing import Sequence


class Solution:
    def findLongestWord(self, s: str, dictionary: Sequence[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for i in dictionary:
            p = -1
            for j in i:
                try:
                    p = s.index(j, p + 1)
                except ValueError:
                    p = -1
                    break
            if p != - 1:
                return i
        return ''


if __name__ == '__main__':
    print(Solution().findLongestWord("aaa", ["aaa", "aa", "a"]))
