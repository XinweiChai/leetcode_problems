class Solution:
    # def numDistinct(self, s: str, t: str) -> int:
    #     cnt = 0
    #
    #     def rec(s, t):
    #         nonlocal cnt
    #         if not t:
    #             cnt += 1
    #             return
    #         if len(s) < len(t):
    #             return
    #         if s[0] == t[0]:
    #             self.numDistinct(s[1:], t[1:])
    #         self.numDistinct(s[1:], t)
    #
    #     rec(s, t)
    #     return cnt
    # def numDistinct(self, s, t):
    #     l1, l2 = len(s) + 1, len(t) + 1
    #     dp = [[1] * l2 for _ in range(l1)]
    #     for j in range(1, l2):
    #         dp[0][j] = 0
    #     for i in range(1, l1):
    #         for j in range(1, l2):
    #             dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (s[i - 1] == t[j - 1])
    #     return dp[-1][-1]

    # O(n) space
    def numDistinct(self, s, t):
        l1, l2 = len(s) + 1, len(t) + 1
        cur = [0] * l2
        cur[0] = 1
        for i in range(1, l1):
            pre = cur[:]
            for j in range(1, l2):
                cur[j] = pre[j] + pre[j - 1] * (s[i - 1] == t[j - 1])
        return cur[-1]


print(Solution().numDistinct(s="rabbbit", t="rabbit"))
