class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        quotient = 0
        sgn = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            temp = 1
            multiply_divisor = divisor
            while dividend >= multiply_divisor:
                multiply_divisor = multiply_divisor << 1
                temp = temp << 1
            dividend -= multiply_divisor >> 1
            quotient += temp >> 1
        if sgn:
            quotient = -quotient
        return quotient


print(Solution().divide(-2147483648, -2))
# print(Solution().divide(10, 3))
