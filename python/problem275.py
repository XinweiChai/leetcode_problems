from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        n = len(citations)
        right = n - 1
        while left <= right:
            mid = (right + left) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left


if __name__ == '__main__':
    print(Solution().hIndex([0]))
