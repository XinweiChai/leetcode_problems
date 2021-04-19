class Solution(object):
    def numDecodings(self, s: str) -> int:
        count = [0] * (len(s) + 2)
        count[-1], count[-2] = 1, 1
        for i in range(len(s) - 1, -1, -1):
            one = count[i + 1] if 1 <= int(s[i]) <= 9 else 0
            two = count[i + 2] if 10 <= int(s[i:i + 2]) <= 26 else 0
            count[i] = one + two
        return count[0]


print(Solution().numDecodings("10"))
