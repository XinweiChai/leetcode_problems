from typing import Sequence


class Solution:
    def maxArea(self, height: Sequence[int]) -> int:
        left = 0
        right = len(height) - 1
        max_val = 0
        while left != right:
            max_val = max(max_val, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_val


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
