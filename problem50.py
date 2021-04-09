class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype -> float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        else:
            return self.myPow(x, n % 2) * self.myPow(x, n // 2) ** 2


print(Solution().myPow(2, -50))
