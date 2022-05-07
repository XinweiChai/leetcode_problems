from typing import Sequence
from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: Sequence[Sequence[int]], k: int) -> int:
        # O(log(m*n))
        # return sorted([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))])[k - 1]

        # Binary search via min VALUE and max VALUE instead of INDEX
        # def count_less_equal(matrix, mid, smaller, larger):
        #     count, n = 0, len(matrix)
        #     row, col = n - 1, 0
        #     while row >= 0 and col < n:
        #         if matrix[row][col] > mid:
        #             # as matrix[row][col] is bigger than the mid, let's keep track of the
        #             # smallest number greater than the mid
        #             larger = min(larger, matrix[row][col])
        #             row -= 1
        #         else:
        #             # as matrix[row][col] is less than or equal to the mid, let's keep track of the
        #             # biggest number less than or equal to the mid
        #             smaller = max(smaller, matrix[row][col])
        #             count += row + 1
        #             col += 1
        #
        #     return count, smaller, larger
        #
        # n = len(matrix)
        # start, end = matrix[0][0], matrix[n - 1][n - 1]
        # while start < end:
        #     mid = start + (end - start) / 2
        #     smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])
        #
        #     count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)
        #
        #     if count == k:
        #         return smaller
        #     if count < k:
        #         start = larger  # search higher
        #     else:
        #         end = smaller  # search lower
        #
        # return start

        # Using min heap
        minHeap = []

        # put the 1st element of each row in the min heap
        # we don't need to push more than 'k' elements in the heap
        for i in range(min(k, len(matrix))):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))

        # take the smallest(top) element form the min heap, if the running count is equal to k' return the number
        # if the row of the top element has more elements, add the next element to the heap
        numberCount, number = 0, 0
        while minHeap:
            number, i, row = heappop(minHeap)
            numberCount += 1
            if numberCount == k:
                break
            if len(row) > i + 1:
                heappush(minHeap, (row[i + 1], i + 1, row))
        return number


print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
