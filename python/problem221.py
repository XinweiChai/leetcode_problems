from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Bad implementation
        # r = len(matrix)
        # c = len(matrix[0])
        # cur = [0] * c
        # max_side = 0
        # for i in range(0, r):
        #     aux = [0] * r
        #     for j in range(c):
        #         cur[j] = 0 if matrix[i][j] == '0' else cur[j] + 1
        #         max_so_far = 0
        #         for k in range(cur[j]):
        #             aux[k] += 1
        #             if aux[max_so_far] >= max_so_far + 1:
        #                 max_so_far += 1
        #                 max_side = max(max_side, max_so_far)
        #         for k in range(cur[j], r):
        #             aux[k] = 0
        # return max_side ** 2

        # DP
        r = len(matrix)
        c = len(matrix[0])
        max_side = 0
        prev = 0
        dp = [0] * (c + 1)
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(prev, dp[j], dp[j - 1]) + 1
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return max_side ** 2


print(Solution().maximalSquare(matrix=[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                                       ["1", "0", "0", "1", "0"]]))
