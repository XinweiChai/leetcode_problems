import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row_size, col_size = len(matrix), len(matrix[0])
        if any(k in row for row in matrix):
            return k
        ans = float('-inf')

        for y1 in range(col_size):

            prefix_sums = [0] * row_size

            for y2 in range(y1, col_size):

                for row in range(row_size):
                    prefix_sums[row] += matrix[row][y2]

                result_big = float('-inf')
                result_small = float('inf')

                cur_big_sum = 0
                cur_small_sum = 0

                for x in prefix_sums:

                    if cur_big_sum < 0:
                        cur_big_sum = x
                    else:
                        cur_big_sum += x

                    if cur_big_sum > result_big:
                        result_big = cur_big_sum

                    if cur_small_sum > 0:
                        cur_small_sum = x
                    else:
                        cur_small_sum += x

                    if cur_small_sum < result_small:
                        result_small = cur_small_sum

                if result_big <= k:
                    ans = max(ans, result_big)
                    if ans == k:
                        return k
                    continue
                if result_small > k:
                    continue

                cur, my_arr, local_res = 0, [0], ans
                for x in prefix_sums:
                    cur += x
                    if my_arr[-1] >= cur - k:
                        local_res = max(local_res, cur - my_arr[bisect.bisect_left(my_arr, cur - k)])
                    bisect.insort(my_arr, cur)
                ans = local_res
                if ans == k:
                    return k
        return ans
