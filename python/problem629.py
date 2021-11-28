from functools import cache


class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if k == 0:
            return 1
        return sum(self.kInversePairs(n - 1, k - i) for i in range(min(k + 1, n))) % 1000000007

    def kInversePairs2(self, n: int, k: int) -> int:
        arr = [1] + [0] * k

        for i in range(2, n + 1):
            for j in range(1, k + 1):
                arr[j] += arr[j - 1]

            for j in range(k, i - 1, -1):
                arr[j] -= arr[j - i]

        # solution requires answer modulo 10^9 + 7
        return arr[k] % (10 ** 9 + 7)


if __name__ == '__main__':
    # print(Solution().kInversePairs(100, 100))
    # print(Solution().kInversePairs2(100, 100))
    print(Solution().kInversePairs(3, 3))
    print(Solution().kInversePairs2(3, 3))
