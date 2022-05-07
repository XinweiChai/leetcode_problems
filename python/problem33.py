from typing import Sequence


class Solution:
    def search(self, nums: Sequence[int], target: int) -> int:
        def rec_search(left, right):
            if left == right:
                return left if nums[left] == target else -1
            mid = (left + right) // 2
            if nums[left] <= target <= nums[mid] or (
                    nums[mid + 1] <= nums[right] and not nums[mid + 1] <= target <= nums[right]):
                return rec_search(left, mid)
            else:
                return rec_search(mid + 1, right)

        return rec_search(0, len(nums) - 1)


print(Solution().search([5, 1, 3], 1))
