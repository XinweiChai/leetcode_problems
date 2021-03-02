class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend > pow(2, 31) - 1 or dividend < -pow(2, 31):
            return pow(2, 31) - 1
        sgn = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        if sgn:
            quotient = -quotient
        return quotient


print(Solution().divide(-2147483648, -2))
