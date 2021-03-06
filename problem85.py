class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def rec(left, right):
            if left == right:
                return 0
            min_col = min(heights[left:right])
            indices = [i for i in range(left, right) if heights[i] == min_col]
            cand = []
            begin = left
            for i in indices:
                cand.append((begin, i))
                begin = i + 1
            cand.append((begin, right))
            temp = [rec(i[0], i[1]) for i in cand]
            return max([min_col * (right - left)] + temp)

        if not matrix or not matrix[0]:
            return 0
        c = len(matrix[0])
        heights = [0] * c
        max_area = 0
        for i in matrix:
            for j in range(len(i)):
                if i[j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            max_area = max(max_area, rec(0, len(heights)))
        return max_area

print(Solution().maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
