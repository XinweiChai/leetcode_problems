from collections import defaultdict
from typing import Sequence


class Solution:
    def countQuadruplets(self, nums: Sequence[int]) -> int:
        # We are looking for a < b < c < d that satisfies equation nums[a] + nums[b] == nums[d] - nums[c]
        n = len(nums)
        res = 0
        d = defaultdict(int)
        d[nums[0] + nums[1]] = 1  # intial count for i == 2
        for i in range(2, n - 1):
            for j in range(i + 1, n):
                # i < j, i => c and j => d
                res += d[nums[j] - nums[i]]  # look for counts of result of right hand side of the equation with nums[i]

            for j in range(i):
                # i > j, i => b and j => a
                d[nums[i] + nums[j]] += 1  # add new sums with nums[i] of left hand side to the dictionary

        return res
