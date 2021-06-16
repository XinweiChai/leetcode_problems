from typing import List
import heapq


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = [float('inf')]
        large = [float('inf')]
        res = []
        for idx, i in enumerate(nums):
            if i < -small[0]:
                heapq.heappush(small, i)
            elif i > large[0]:
                heapq.heappush(large, i)
            else:
                if len(small) > len(large):
                    heapq.heappush(large, i)
                else:
                    heapq.heappush(small, -i)
            if len(small) - len(large) > 1:
                heapq.heappush(large, heapq.heappop(small))
            if len(large) - len(small) > 1:
                heapq.heappush(small, heapq.heappop(large))
            if idx >= k - 1:
                if k % 2 == 0:
                    res.append((large[0] - small[0]) / 2)
                else:
                    res.append(float(-small[0]))
        return res


if __name__ == '__main__':
    print(Solution().medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
