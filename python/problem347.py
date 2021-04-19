from collections import Counter
import heapq
from typing import List
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(Nlogk)
        # c = Counter(nums)
        # return heapq.nlargest(k, c.keys(), key=c.get)

        # QuickSelect O(n)
        c = Counter(nums)
        c = list(c.items())

        # def quick_select(l, r):
        #     pivot = random.randrange(l, r)
        #     c[pivot], c[l] = c[l], c[pivot]
        #     top = r - 1
        #     i = r
        #     while l < i - 1:
        #         if c[l][1] <= c[i - 1][1]:
        #             c[i - 1], c[top] = c[top], c[i - 1]
        #             top -= 1
        #         i -= 1
        #     c[l], c[top] = c[top], c[l]
        #     if top < len(c) - k:
        #         quick_select(top + 1, r)
        #     elif top > len(c) - k:
        #         quick_select(l, top)
        #
        # quick_select(0, len(c))
        # return [c[-i][0] for i in range(1, k + 1)]

        def quick_select(l, r):
            pivot = random.randrange(l, r)
            c[pivot], c[r - 1] = c[r - 1], c[pivot]
            low = l
            for i in range(l, r - 1):
                if c[i][1] <= c[r - 1][1]:
                    c[i], c[low] = c[low], c[i]
                    low += 1
            c[r - 1], c[low] = c[low], c[r - 1]
            if low > len(c) - k:
                quick_select(l, low)
            elif low < len(c) - k:
                quick_select(low + 1, r)

        quick_select(0, len(c))
        return [c[-i][0] for i in range(1, k + 1)]


# print(Solution().topKFrequent([1, 1, 1, 1, 2, 2, 3], 2))
# print(Solution().topKFrequent([3,0,1,0],1))
print(Solution().topKFrequent(
    [5, 1, -1, -8, -7, 8, -5, 0, 1, 10, 8, 0, -4, 3, -1, -1, 4, -5, 4, -3, 0, 2, 2, 2, 4, -2, -4, 8, -7, -7, 2, -8, 0,
     -8, 10, 8, -8, -2, -9, 4, -7, 6, 6, -1, 4, 2, 8, -3, 5, -9, -3, 6, -8, -5, 5, 10, 2, -5, -1, -5, 1, -3, 7, 0, 8,
     -2, -3, -1, -5, 4, 7, -9, 0, 2, 10, 4, 4, -4, -1, -1, 6, -8, -9, -1, 9, -9, 3, 5, 1, 6, -1, -2, 4, 2, 4, -6, 4, 4,
     5, -5], 7))
# print(Solution().topKFrequent([4,1,-1,2,-1,2,3],2))
