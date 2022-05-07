from typing import Sequence


class Solution:
    def increasingTriplet(self, nums: Sequence[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


# print(Solution().increasingTriplet([1, 2, 3, 4, 5]))
# print(Solution().increasingTriplet([6, 7, 1, 2]))
print(Solution().increasingTriplet([0, 4, -1, 2]))
