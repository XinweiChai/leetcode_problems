from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:  # n lies between min1 and min2
                min2 = n
            if n >= max1:  # n is greater than max1, max2 and max3
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:  # n lies between max1 and max2
                max3 = max2
                max2 = n
            elif n >= max3:  # n lies between max2 and max3
                max3 = n

        return max(min1 * min2 * max1, max1 * max2 * max3)
