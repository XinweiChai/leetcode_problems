class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 1
        total = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            total += (ord(columnTitle[i]) - ord('A') + 1) * base
            base *= 26
        return total


print(Solution().titleToNumber("FXSHRXW"))
