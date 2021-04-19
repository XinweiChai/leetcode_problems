from typing import List


class Solution(object):
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans

#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         left_limit = 0
#         top_limit = 0
#         right_limit = len(matrix[0]) - 1
#         bottom_limit = len(matrix) - 1
#         x = 0
#         y = 0
#         res = [matrix[0][0]]
#         while left_limit <= right_limit and top_limit <= bottom_limit:
#             while x < right_limit and left_limit <= right_limit and top_limit <= bottom_limit:
#                 x += 1
#                 res.append(matrix[y][x])
#             top_limit += 1
#             while y < bottom_limit and left_limit <= right_limit and top_limit <= bottom_limit:
#                 y += 1
#                 res.append(matrix[y][x])
#             right_limit -= 1
#             while x > left_limit and left_limit <= right_limit and top_limit <= bottom_limit:
#                 x -= 1
#                 res.append(matrix[y][x])
#             bottom_limit -= 1
#             while y > top_limit and left_limit <= right_limit and top_limit <= bottom_limit:
#                 y -= 1
#                 res.append(matrix[y][x])
#             left_limit += 1
#         return res
#
#
# print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
