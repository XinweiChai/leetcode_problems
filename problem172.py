class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        base = 1
        base_count = 0
        while base <= n:
            base_count += 1
            base *= 5
        base //= 5
        base_count -= 1
        zeros = 0
        while base != 1:
            zeros += n // base
            base //= 5
            base_count -= 1
        return zeros


print(Solution().trailingZeroes(100))
