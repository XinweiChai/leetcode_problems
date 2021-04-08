import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i + 1 for i in range(n)]
        fac = [math.factorial(i) for i in range(n)]
        s = ''
        k -= 1
        for i in range(n):
            idx = k // fac[n - i - 1]
            s += str(nums.pop(idx))
            k -= idx * fac[n - i - 1]
        return s


print(Solution().getPermutation(2, 1))
