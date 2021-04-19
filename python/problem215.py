from typing import List
import heapq
import random

class Solution:
    # O(n), quick selection
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthSmallest(nums, len(nums) + 1 - k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    # put the pivot in the right place (left < pivot right>pivot)
    def partition(self, nums, l, r):
        low = l
        ri = random.randint(l, r)
        nums[r], nums[ri] = nums[ri], nums[r]
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

        # Using heap, O(n+(n-k)lnn)
        # return heapq.nlargest(k, nums)[-1]


print(Solution().findKthLargest([3, 4, 2, 3, 1, 2, 4, 5, 5, 6, 4, 1.5], 6))
