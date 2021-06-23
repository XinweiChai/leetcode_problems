class Solution:
    def countDigitOne(self, n: int) -> int:
        ones = 0
        digit = 1
        while digit <= n:
            ones += digit * (n // (digit * 10)) + min(digit, max(0, n % (digit * 10) - digit + 1))
            digit *= 10
        return ones


if __name__ == '__main__':
    print(Solution().countDigitOne(100))
