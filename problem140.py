class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)

        dp_table = [False] * len(s)
        comb = [[] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            if s[i:] in wordDict:
                dp_table[i] = True
                comb[i].append(len(s))
            for j in range(i + 1, len(s)):
                if dp_table[j] and s[i:j] in wordDict:
                    dp_table[i] = True
                    comb[i].append(j)
        ans = []

        def rec(pos, cand):
            if pos < len(s):
                for i in comb[pos]:
                    rec(i, cand + s[pos:i] + ' ')
            else:
                ans.append(cand[:-1])

        rec(0, '')
        return ans


# print(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(Solution().wordBreak("aaaaaaa", ["aaaa", "aa", "a"]))
