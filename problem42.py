class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p = 0

        def find_right(p_left):
            if height[p_left] >= max(height[p_left + 1:]):
                return height[p_left + 1:].index(max(height[p_left + 1:])) + p_left + 1
            else:
                for i in range(p_left + 1, len(height)):
                    if height[i] > height[p_left]:
                        return i

        def count_water(left, right):
            volume = 0
            for i in range(left + 1, right):
                volume += min(height[left], height[right]) - height[i]
            return volume

        res = 0
        while p < len(height) - 1:
            right = find_right(p)
            res += count_water(p, right)
            p = right
        return res


# print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([]))
