from typing import Sequence
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: Sequence[Sequence[int]]) -> int:
        def lengthOfLIS(nums):
            dp = [0] * len(nums)
            l = 0
            for num in nums:
                i = bisect.bisect_left(dp, num, hi=l)
                dp[i] = num
                if i == l:
                    l += 1
            return l

        envelopes.sort(key=lambda x: [x[0], -x[1]])

        return lengthOfLIS([i[1] for i in envelopes])


if __name__ == '__main__':
    print(Solution().maxEnvelopes([[30, 50], [12, 2], [3, 4], [12, 15]]))
