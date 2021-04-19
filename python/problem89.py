from typing import List


class Solution(object):
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = i ^ (i >> 1)
        return ans


print(Solution().grayCode(3))
