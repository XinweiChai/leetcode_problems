class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)

        dp_table = [False] * len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i:] in wordDict:
                dp_table[i] = True
            else:
                for j in range(i + 1, len(s)):
                    if dp_table[j] and s[i:j] in wordDict:
                        dp_table[i] = True
                        break

        return dp_table[0]


print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    , ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
