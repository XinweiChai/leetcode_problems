class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        res = 0

        def rec(left, right):
            global res
            if left == right:
                return 0
            # if right - left == 1:
            #     return heights[left]
            min_col = min(heights[left:right])
            indices = [i for i in range(left, right) if heights[i] == min_col]
            cand = []
            begin = left
            for i in indices:
                cand.append((begin, i))
                begin = i + 1
            cand.append((begin, right))
            for i in cand:
                res = max(res, rec(i[0], i[1]))
            return max([min_col * (right - left - 1)] + res)

        return rec(0, len(heights))


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
