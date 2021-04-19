class Solution:
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     # 2D DP
    #     if len(s1) + len(s2) != len(s3):
    #         return False
    #     dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    #     dp[0][0] = True
    #     for i in range(1, len(s1) + 1):
    #         dp[i][0] = dp[i - 1][0] and s3[i - 1] == s1[i - 1]
    #     for j in range(1, len(s2) + 1):
    #         dp[0][j] = dp[0][j - 1] and s3[j - 1] == s2[j - 1]
    #     for i in range(1, len(s1) + 1):
    #         for j in range(1, len(s2) + 1):
    #             dp[i][j] = (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (
    #                         dp[i][j - 1] and s3[i + j - 1] == s2[j - 1])
    #     return dp[len(s1)][len(s2)]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 1D DP
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s1) + 1)
        dp[0] = True
        for i in range(len(s1)):
            dp[i + 1] = dp[i] and s3[i] == s1[i]
        for j in range(len(s2)):
            dp[0] = dp[0] and s3[j] == s2[j]
            for i in range(len(s1)):
                dp[i + 1] = (dp[i] and s3[i + j + 1] == s1[i]) or (dp[i + 1] and s3[i + j + 1] == s2[j])
        return dp[len(s1)]


print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
print(Solution().isInterleave(s1="", s2="b", s3="b"))
