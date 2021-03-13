from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return heapq.nlargest(k, c.keys(), key=c.get)


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
