class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP, using O(n^2) space
        # r = len(word1)
        # c = len(word2)
        # dp = [[0] * (c + 1) for _ in range(r + 1)]
        # for i in range(r + 1):
        #     dp[i][0] = i
        # for i in range(c + 1):
        #     dp[0][i] = i
        # for i in range(1, r + 1):
        #     for j in range(1, c + 1):
        #         temp = dp[i - 1][j - 1]
        #         if word1[i - 1] != word2[j - 1]:
        #             temp += 1
        #         dp[i][j] = min(temp, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        # return dp[r][c]

        # DP, using only one list (O(n)) to store the intermediate values
        r = len(word1)
        c = len(word2)
        dp = [i for i in range(c + 1)]
        for i in range(1, r + 1):
            dp[0] = i
            temp = i - 1
            for j in range(1, c + 1):
                if word1[i - 1] != word2[j - 1]:
                    temp += 1
                # Store dp[i - 1][j - 1]
                before = dp[j]
                dp[j] = min(temp, dp[j - 1] + 1, dp[j] + 1)
                temp = before
        return dp[c]


print(Solution().minDistance("a", ""))
print(Solution().minDistance("aeea", "ebeb"))
print(Solution().minDistance("intention", "execution"))
print(Solution().minDistance("plasma", "altruism"))
