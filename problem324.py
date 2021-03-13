from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Using sort, O(nlogn) time
        # nums.sort()
        # half = len(nums[::2])
        # nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

        # Index-rewiring


print(Solution().wiggleSort([1, 5, 1, 1, 6, 4]))
# print(Solution().wiggleSort([1, 3, 2, 2, 3, 1]))
