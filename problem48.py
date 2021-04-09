from typing import List


class Solution(object):
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        side = len(matrix)
        for i in range(side // 2):
            for j in range((side + 1) // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[side - 1 - j][i]
                matrix[side - 1 - j][i] = matrix[side - 1 - i][side - 1 - j]
                matrix[side - 1 - i][side - 1 - j] = matrix[j][side - 1 - i]
                matrix[j][side - 1 - i] = temp


print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
