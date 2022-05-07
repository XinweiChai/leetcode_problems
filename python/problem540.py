from typing import Sequence


class Solution:
    def singleNonDuplicate(self, nums: Sequence[int]):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


    def singleNonDuplicate2(self, nums: Sequence[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if (mid - low) % 2 != 0:
                if nums[mid] != nums[mid - 1]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] != nums[mid + 1]:
                    high = mid
                else:
                    low = mid

        return nums[low]
if __name__ == '__main__':
    print(Solution().singleNonDuplicate(nums=[1, 1, 2]))
