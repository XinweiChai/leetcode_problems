from functools import lru_cache


# Recursive solution, need exponential time, but can be optimized by lru_cache
class Solution:
    @lru_cache
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = s and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


# DP solution, need O(SP) time
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    memo[i, j] = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in [s[i], '.']
                    if j < len(p) - 1 and p[j + 1] == '*':
                        memo[i, j] = dp(i, j + 2) or (first_match and dp(i + 1, j))
                    else:
                        memo[i, j] = first_match and dp(i + 1, j + 1)
            return memo[i, j]

        return dp(0, 0)


class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache()
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            else:
                first_match = i < len(s) and p[j] in [s[i], '.']
                if j < len(p) - 1 and p[j + 1] == '*':
                    return dp(i, j + 2) or (first_match and dp(i + 1, j))
                else:
                    return first_match and dp(i + 1, j + 1)

        return dp(0, 0)

print(Solution2().isMatch("mississippi", "p*"))
