from typing import Sequence


class Solution:
    # Using O(nlogn) time and O(1) space
    def hIndex(self, citations: Sequence[int]) -> int:
        citations.sort(reverse=True)
        for idx, i in enumerate(citations):
            if idx + 1 > i:
                return idx
        return len(citations)

    def hIndex2(self, citations: Sequence[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        for i in citations:
            if i > n:
                buckets[n] += 1
            else:
                buckets[i] += 1
        cnt = 0
        for i in range(n, -1, -1):
            cnt += buckets[i]
            if cnt >= i:
                return i
        return 0


if __name__ == '__main__':
    print(Solution().hIndex(citations=[3, 0, 6, 1, 5]))
