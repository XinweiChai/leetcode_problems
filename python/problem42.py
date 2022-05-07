from typing import Sequence


class Solution:
    def trap(self, height: Sequence[int]) -> int:
        # p = 0
        #
        # def find_right(p_left):
        #     if height[p_left] >= max(height[p_left + 1:]):
        #         return height[p_left + 1:].index(max(height[p_left + 1:])) + p_left + 1
        #     else:
        #         for i in range(p_left + 1, len(height)):
        #             if height[i] > height[p_left]:
        #                 return i
        #
        # def count_water(left, right):
        #     volume = 0
        #     for i in range(left + 1, right):
        #         volume += min(height[left], height[right]) - height[i]
        #     return volume
        #
        # res = 0
        # while p < len(height) - 1:
        #     right = find_right(p)
        #     res += count_water(p, right)
        #     p = right
        # return res

        # DP
        # if not height:
        #     return 0
        # ans = 0
        # size = len(height)
        # left_max = [0] * size
        # right_max = [0] * size
        # left_max[0] = height[0]
        # right_max[size - 1] = height[size - 1]
        # for i in range(1, size):
        #     left_max[i] = max(height[i], left_max[i - 1])
        # for i in range(size - 2, -1, -1):
        #     right_max[i] = max(height[i], right_max[i + 1])
        # for i in range(1, size - 1):
        #     ans += min(left_max[i], right_max[i]) - height[i]
        # return ans

        # Stack
        ans = 0
        current = 0
        st = []
        while current < len(height):
            while st and height[current] > height[st[-1]]:
                top = st[-1]
                st.pop()
                if not st:
                    break
                distance = current - st[-1] - 1
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                ans += distance * bounded_height
            st.append(current)
            current += 1
        return ans


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# print(Solution().trap([]))
