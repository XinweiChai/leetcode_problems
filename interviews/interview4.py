class Solution(object):
    def numDecodings(self, s: str) -> int:
        cnt = [0] * (len(s) + 2)
        cnt[-1], cnt[-2] = 1, 1
        for i in range(len(s) - 1, -1, -1):
            cnt[i] += cnt[i + 1] if 1 <= int(s[i]) <= 9 else 0
            cnt[i] += cnt[i + 2] if 10 <= int(s[i:i + 2]) <= 26 else 0
        return cnt[0]


print(Solution().numDecodings(""))
