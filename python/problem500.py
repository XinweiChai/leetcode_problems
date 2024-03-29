from typing import Sequence


class Solution:
    def findWords(self, words: Sequence[str]) -> Sequence[str]:
        lines = [set(i) for i in ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]]
        res = [i for i in words for j in lines if set(i).issubset(j)]
        return res

if __name__ == '__main__':
    print(Solution().findWords(words = ["Hello","Alaska","Dad","Peace"]))