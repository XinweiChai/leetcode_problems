import re


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Recursion
        # if not p:
        #     return not s
        # first_match = bool(s) and p[0] in ['?', s[0]]
        # if p[0] == '*':
        #     if not s or (len(p) > 1 and p[1] == '*'):
        #         return self.isMatch(s, p[1:])
        #     else:
        #         return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])

        # Dynamic programming top-down
        # mem = {}
        #
        # def dp(i, j):
        #     if (i, j) not in mem:
        #         if j == len(p):
        #             ans = i == len(s)
        #         else:
        #             first_match = i < len(s) and p[j] in ['?', s[i]]
        #             if p[j] == '*':
        #                 if i == len(s) or (j < len(p) - 1 and p[j + 1] == '*'):
        #                     ans = dp(i, j + 1)
        #                 else:
        #                     ans = dp(i, j + 1) or dp(i + 1, j)
        #             else:
        #                 ans = first_match and dp(i + 1, j + 1)
        #         mem[i, j] = ans
        #     return mem[i, j]
        #
        # return dp(0, 0)

        # Dynamic programming bottom-up
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in ['?', s[i]]
                if p[j] == '*':
                    if i == len(s) or (j < len(p) - 1 and p[j + 1] == '*'):
                        dp[i][j] = dp[i][j + 1]
                    else:
                        dp[i][j] = dp[i][j + 1] or dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]


print(Solution().isMatch("", "*c"))
