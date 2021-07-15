from typing import List
import heapq


class Solution:
    """
    # # # # # # ?
    # # # ?
    # ?
    # x
    # x
    ?

    used_line is to avoid the push of position x
    """

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        used_line = [False] * len(nums1)

        def push(i, j):
            if i < len(nums1) and j < len(nums2) and not used_line[i]:
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
                used_line[i] = True

        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            used_line[i] = False
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs


if __name__ == '__main__':
    print(Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=10))
