from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> bool:
        # Cheat with O(n)
        # return target in nums
        def fast_bin_search(start, end):
            if start == end:
                return target == nums[start]
            mid = (start + end) // 2
            if nums[mid] >= target:
                return fast_bin_search(start, mid)
            else:
                return fast_bin_search(mid + 1, end)

        def bin_search(start, end):
            if start == end:
                return target == nums[start]
            mid = (start + end) // 2
            if nums[mid] >= target >= nums[start]:
                return fast_bin_search(start, mid)
            elif nums[mid + 1] <= target <= nums[end]:
                return fast_bin_search(mid + 1, end)
            else:
                return bin_search(start, mid) or bin_search(mid + 1, end)

        return bin_search(0, len(nums) - 1)


print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0))
