import bisect
# available from Python3.9
# from functools import cache
from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # @cache
        @lru_cache(maxsize=None)
        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return 2 + dp(l + 1, r - 1)
            else:
                return max(dp(l + 1, r), dp(l, r - 1))

        return dp(0, len(s) - 1)

    def longestPalindromeSubseq2(self, s: str) -> int:
        indexes = [[] for _ in range(26)]
        for idx, i in enumerate(s):
            indexes[ord(i) - ord('a')].append(idx)
        memo = {}

        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if (l, r) in memo:
                return memo[l, r]
            if s[l] == s[r]:
                return 2 + dp(l + 1, r - 1)
            else:
                c_l = ord(s[l]) - ord('a')
                c_r = ord(s[r]) - ord('a')
                x = indexes[c_l][bisect.bisect(indexes[c_l], r) - 1]
                y = indexes[c_r][bisect.bisect(indexes[c_r], l)]
                memo[l, x] = dp(l, x)
                memo[y, r] = dp(y, r)
                return max(dp(l + 1, r - 1), dp(l, x), dp(y, r))

        return dp(0, len(s) - 1)

    def longestPalindromeSubseq3(self, s: str) -> int:
        d = {}

        def helper(x):
            if x not in d:
                r = 0
                for i in set(x):
                    a, b = x.find(i), x.rfind(i)
                    r = max(r, 1 if a == b else 2 + helper(x[a + 1:b]))
                d[x] = r
            return d[x]

        return helper(s)

    # with less memory
    def longestPalindromeSubseq4(self, s: str) -> int:
        indexes = [[] for _ in range(26)]
        for idx, i in enumerate(s):
            indexes[ord(i) - ord('a')].append(idx)
        d = {}

        def helper(left, right):
            if (left, right) not in d:
                r = 0
                for i in indexes:
                    if i and i[0] <= right and i[-1] >= left:
                        a = i[bisect.bisect_left(i, left)]
                        b = i[bisect.bisect(i, right) - 1]
                        if a <= b:
                            r = max(r, b - a + 1 if a >= b - 1 else 2 + helper(a + 1, b - 1))
                d[left, right] = r
            return d[left, right]

        return helper(0, len(s) - 1)


if __name__ == '__main__':
    print(Solution().longestPalindromeSubseq("abcabcabcabc"))
