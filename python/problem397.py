from functools import lru_cache


class Solution:
    @lru_cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n & 1:
            return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1
        return self.integerReplacement(n // 2) + 1

    # O(1) space
    def integerReplacement2(self, n):
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn


if __name__ == '__main__':
    print(Solution().integerReplacement(7))
