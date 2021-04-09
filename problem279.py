class Solution(object):
    table = {}

    def numSquares(self, n: int) -> int:
        # if n in self.table:
        #     return self.table[n]
        # trial_max = int(n ** 0.5)
        # trial_min = max(int((n / 3) ** 0.5), 1)
        # if n == trial_max ** 2:
        #     decomp = 1
        # else:
        #     min_comb = float('inf')
        #     for i in range(trial_max, trial_min - 1, -1):
        #         temp = self.numSquares(n - i ** 2)
        #         if temp == 1:
        #             min_comb = 1
        #             break
        #         min_comb = min(min_comb, temp)
        #     decomp = 1 + min_comb
        # self.table[n] = decomp
        # return decomp

        # Lagrange's Four Square theorem
        def is_square(n):
            return n - int(n ** 0.5) ** 2 == 0

        if is_square(n):
            return 1
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        sqrt_n = int(n ** 0.5)
        for i in range(1, sqrt_n + 1):
            if is_square(n - i * i):
                return 2
        return 3


print(Solution().numSquares(12))
