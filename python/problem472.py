from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        memo = {}

        def find(w, concat):
            if (w, concat) not in memo:
                if not w:
                    return concat
                for j in range(len(w) + concat - 1, 0, -1):
                    if w[:j] in words and find(w[j:], True):
                        memo[(w, concat)] = True
                        return True
                memo[(w, concat)] = False
                return False
            return memo[(w, concat)]
        res = [i for i in words if find(i, False)]

        return res


if __name__ == '__main__':
    print(Solution().findAllConcatenatedWordsInADict(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
    # print(Solution().findAllConcatenatedWordsInADict(["cat", "dog", "catdog"]))
    # print(Solution().findAllConcatenatedWordsInADict())