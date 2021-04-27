from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find mid then search extreme
        # if not nums or target < nums[0] or target > nums[-1]:
        #     return [-1, -1]
        #
        # def search(left, right):
        #     if left == right:
        #         return left if target == nums[left] else -1
        #     mid = (left + right) // 2
        #     if target <= nums[mid]:
        #         return search(left, mid)
        #     else:
        #         return search(mid + 1, right)
        #
        # pos = search(0, len(nums) - 1)
        # if pos == -1:
        #     return [-1, -1]
        # ans = [pos, pos]
        # if nums[0] == target:
        #     ans[0] = 0
        # elif nums[pos - 1] == target:
        #     pos1 = pos
        #     while pos1 != -1 and pos1 > 0:
        #         ans[0] = pos1
        #         pos1 = search(0, pos1 - 1)
        # if nums[-1] == target:
        #     ans[1] = len(nums) - 1
        # elif nums[pos + 1] == target:
        #     pos2 = pos
        #     while pos2 != -1 and pos2 < len(nums) - 1:
        #         ans[1] = pos2
        #         pos2 = search(pos2 + 1, len(nums) - 1)
        # return ans

        # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
        # array `nums` via binary search.

        def extreme_insertion_index(nums, target, left):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        left_idx = extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, extreme_insertion_index(nums, target, False) - 1]


print(Solution().searchRange([5, 7, 7, 8, 8, 8], 8))
