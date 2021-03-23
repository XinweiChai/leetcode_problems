from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c1 = Counter(p)
        c2 = Counter(s[:len(p)])
        satisfied = 0
        ans = []
        for i in c2:
            if c2[i] == c1[i]:
                satisfied += 1
        if satisfied == len(c1):
            ans.append(0)
        for i in range(len(s) - len(p)):
            if s[i] in c1:
                if c2[s[i]] == c1[s[i]]:
                    satisfied -= 1
                c2[s[i]] -= 1
                if c2[s[i]] == c1[s[i]]:
                    satisfied += 1
            if s[i + len(p)] in c1:
                if c2[s[i + len(p)]] == c1[s[i + len(p)]]:
                    satisfied -= 1
                c2[s[i + len(p)]] += 1
                if c2[s[i + len(p)]] == c1[s[i + len(p)]]:
                    satisfied += 1
            if satisfied == len(c1):
                ans.append(i + 1)
        return ans


print(Solution().findAnagrams("cbaebabacd", "abc"))
print(Solution().findAnagrams("abacbabc", "abc"))
print(Solution().findAnagrams("baa", "aa"))
