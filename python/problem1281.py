import operator
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        A = [int(n) for n in str(n)]
        return reduce(operator.mul, A) - sum(A)


if __name__ == '__main__':
    print(Solution().subtractProductAndSum(234))