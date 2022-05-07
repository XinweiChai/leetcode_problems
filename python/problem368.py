from typing import Sequence


class Solution:
    def largestDivisibleSubset(self, nums: Sequence[int]) -> Sequence[int]:
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len).union({x})
        return list(max(S.values(), key=len))


if __name__ == '__main__':
    print(Solution().largestDivisibleSubset([5, 9, 18, 54, 108, 540, 90, 180, 360, 720]))
