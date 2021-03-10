class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            digit = n & 1
            n = n >> 1
            ans = (ans << 1) + digit
        return ans


print(Solution().reverseBits(43261596))
