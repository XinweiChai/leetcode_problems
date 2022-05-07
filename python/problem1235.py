from typing import Sequence
import bisect

class Solution:
    def jobScheduling(self, startTime: Sequence[int], endTime: Sequence[int], profit: Sequence[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]


if __name__ == '__main__':
    print(Solution().jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]))
