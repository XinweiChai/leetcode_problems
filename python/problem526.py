class Solution:
    def countArrangement(self, n: int) -> int:
        cells = [0] * n
        values = [[j - 1 for j in range(1, n + 1) if i % j == 0 or j % i == 0] for i in range(1, n + 1)]

        def bt(x):
            if x == 1:
                return 1
            cnt = 0
            for i in values[x - 1]:
                if cells[i] == 0:
                    cells[i] = x
                    cnt += bt(x - 1)
                    cells[i] = 0
            return cnt

        return bt(n)

    # Space-time tradeoff for faster speed
    def countArrangement2(self, n):
        cache = {}

        def helper(i, X):
            if i == 1:
                return 1
            key = (i, X)
            if key in cache:
                return cache[key]
            total = 0
            for j in range(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:
                    total += helper(i - 1, X[:j] + X[j + 1:])
            cache[key] = total
            return total
        return helper(n, tuple(range(1, n + 1)))

if __name__ == '__main__':
    print(Solution().countArrangement(20))
