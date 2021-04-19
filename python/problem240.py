from typing import List


class Solution(object):
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        # O(r*logc) or O(c*logr)
        # def find_in_row(row, left, right):
        #     if left == right:
        #         return target == matrix[row][left]
        #     mid = (left + right) // 2
        #     if target <= matrix[row][mid]:
        #         return find_in_row(row, left, mid)
        #     else:
        #         return find_in_row(row, mid + 1, right)
        #
        # def find_in_col(col, left, right):
        #     if left == right:
        #         return target == matrix[left][col]
        #     mid = (left + right) // 2
        #     if target <= matrix[mid][col]:
        #         return find_in_col(col, left, mid)
        #     else:
        #         return find_in_col(col, mid + 1, right)
        #
        # if r <= c:
        #     for i in range(r):
        #         if matrix[i][0] <= target <= matrix[i][c - 1] and find_in_row(i, 0, c - 1):
        #             return True
        #     return False
        # else:
        #     for i in range(c):
        #         if matrix[0][i] <= target <= matrix[r - 1][i] and find_in_col(i, 0, r - 1):
        #             return True
        #     return False

        # O(r+c)
        pr = 0
        pc = c - 1
        while pr < r and pc >= 0:
            if target == matrix[pr][pc]:
                return True
            elif target < matrix[pr][pc]:
                pc -= 1
            else:
                pr += 1
        return False


print(Solution().searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
