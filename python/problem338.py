from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # c = [0] * (num + 1)
        # exp = 1
        # for i in range(1, num + 1):
        #     if i == exp:
        #         c[i] = 1
        #         exp *= 2
        #     else:
        #         c[i] = c[i - exp//2] + 1
        # return c

        c = [0] * (num + 1)
        for i in range(1, num + 1):
            c[i] = c[i & (i - 1)] + 1
        return c

print(Solution().countBits(8))
