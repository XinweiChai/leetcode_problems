from typing import Sequence


class Solution:
    def findLUSlength(self, strs: Sequence[str]) -> int:
        def issubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)

        for s in sorted(strs, key=len, reverse=True):
            if sum(issubsequence(s, t) for t in strs) == 1:
                return len(s)
        return -1


if __name__ == '__main__':
    print(Solution().findLUSlength(strs=["aabbcc", "aabbcc","aadd", "aadd", "bc"]))
