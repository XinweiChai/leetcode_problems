from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # O(n^2) solution
        if sum(nums) & 1 == 0:
            target = sum(nums) >> 1
            cur = {0}
            for i in nums:
                cur |= {i + x for x in cur}
                if target in cur:
                    return True
        return False


print(Solution().canPartition([1, 4, 4, 6, 7, 8]))
