from typing import List
from math import factorial


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # return [factorial(rowIndex) // factorial(i) // factorial(rowIndex - i) for i in range(rowIndex + 1)]
        res = [1] * (rowIndex + 1)
        for i in range(1, rowIndex // 2 + 1):
            res[i] = res[i - 1] * (rowIndex - i + 1) // i
            res[~i] = res[i]
        return res


print(Solution().getRow(2))
