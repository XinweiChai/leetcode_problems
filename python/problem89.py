from typing import Sequence


class Solution:
    def grayCode(self, n: int) -> Sequence[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = i ^ (i >> 1)
        return ans


print(Solution().grayCode(3))
