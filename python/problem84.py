from typing import Sequence


class Solution:
    def largestRectangleArea(self, heights: Sequence[int]) -> int:
        # def rec(left, right):
        #     if left == right:
        #         return 0
        #     min_col = min(heights[left:right])
        #     indices = [i for i in range(left, right) if heights[i] == min_col]
        #     cand = []
        #     begin = left
        #     for i in indices:
        #         cand.append((begin, i))
        #         begin = i + 1
        #     cand.append((begin, right))
        #     temp = [rec(i[0], i[1]) for i in cand]
        #     return max([min_col * (right - left)] + temp)

        # return rec(0, len(heights))

        less_from_left = [-1] * len(heights)
        less_from_right = [-1] * len(heights)
        less_from_right[-1] = len(heights)
        less_from_left[0] = -1

        for i in range(1, len(heights)):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_from_left[p]
            less_from_left[i] = p

        for i in range(len(heights) - 2, -1, -1):
            p = i + 1
            while p < len(heights) and heights[p] >= heights[i]:
                p = less_from_right[p]
            less_from_right[i] = p
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i] * (less_from_right[i] - less_from_left[i] - 1))
        return max_area


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
# print(Solution().largestRectangleArea([5, 6, 2, 3]))
