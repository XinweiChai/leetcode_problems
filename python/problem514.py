from functools import lru_cache
import bisect


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)

        # @lru_cache
        memo = {}

        def dfs(cur, p):
            if p == m:
                return 0
            if (cur, p) in memo:
                return memo[cur, p]
            c = key[p]
            if ring[cur] == c:
                memo[cur, p] = dfs(cur, p + 1)
                return memo[cur, p]
            try:
                pl = ring.rindex(c, 0, cur)
            except ValueError:
                pl = ring.rindex(c, cur, n)
            try:
                pr = ring.index(c, cur, n)
            except ValueError:
                pr = ring.index(c, 0, cur)
            if pl == pr:
                memo[cur, p] = min(abs(pr - cur), n - abs(cur - pr)) + dfs(pr, p + 1)
            else:
                memo[cur, p] = min(min(abs(pr - cur), n - abs(cur - pr)) + dfs(pr, p + 1),
                                   min(abs(pl - cur), n - abs(cur - pl)) + dfs(pl, p + 1))
            return memo[cur, p]

        return m + dfs(0, 0)

    def findRotateSteps2(self, ring: str, key: str) -> int:
        N = len(ring)
        K = len(key)

        @lru_cache(None)
        def dp(curRing, idx):
            if idx == K:
                return 0
            char = key[idx]
            leftIdx = curRing.index(char)
            rightIdx = curRing.rindex(char)
            return min(leftIdx + dp(curRing[leftIdx:] + curRing[:leftIdx], idx + 1),
                       (N - rightIdx) + dp(curRing[rightIdx:] + curRing[:rightIdx], idx + 1)) + 1

        return dp(ring, 0)

    def findRotateSteps3(self, ring: str, key: str) -> int:
        pos = {}
        for idx, i in enumerate(ring):
            pos[i] = pos.get(i, []) + [idx]
        n = len(ring)
        m = len(key)
        # @lru_cache
        memo = {}

        def dfs(cur, p):
            if p == m:
                return 0
            if (cur, p) in memo:
                return memo[cur, p]
            c = key[p]
            if len(pos[c]) == 1:
                memo[cur, p] = min(abs(pos[c][0] - cur), n - abs(cur - pos[c][0])) + dfs(pos[c][0], p + 1)
            else:
                idx = bisect.bisect(pos[c], cur)
                pr = pos[c][idx] if idx != len(pos[c]) else pos[c][0]
                pl = pos[c][idx - 1] if idx != 0 else pos[c][-1]
                memo[cur, p] = min(min(abs(pr - cur), n - abs(cur - pr)) + dfs(pr, p + 1),
                                   min(abs(pl - cur), n - abs(cur - pl)) + dfs(pl, p + 1))
            return memo[cur, p]

        return m + dfs(0, 0)


if __name__ == '__main__':
    print(Solution().findRotateSteps3("godding", "godding"))
