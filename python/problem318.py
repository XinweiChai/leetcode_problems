from typing import List
from collections import Counter


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        cnts = []
        res = 0
        for idx, i in enumerate(words):
            cnts.append(Counter(i))
            for j in range(idx):
                if not cnts[j].keys() & cnts[idx].keys():
                    res = max(res, sum(cnts[j].values()) * sum(cnts[idx].values()))
        return res

    # Smarter solution
    def maxProduct2(self, words: List[str]) -> int:
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

if __name__ == '__main__':
    print(Solution().maxProduct2(["abcw", "xtfn", "baz", "foo", "bar", "abcdef"]))
