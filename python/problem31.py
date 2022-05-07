from typing import Sequence


class Solution:
    def nextPermutation(self, nums: Sequence[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        # Find the first decreasing element
        for p in range(n - 1, -2, -1):
            if nums[p] < nums[p + 1]:
                break
        # Find the element to swap with
        if p >= 0:
            if nums[n] > nums[p]:
                nums[n], nums[p] = nums[p], nums[n]
            else:
                for i in range(p + 1, n):
                    if nums[i] > nums[p] >= nums[i + 1]:
                        nums[i], nums[p] = nums[p], nums[i]
                        break
        # Reverse the sublist after position p
        # p += 1
        # while p < n:
        #     nums[p], nums[n] = nums[n], nums[p]
        #     p += 1
        #     n -= 1
        nums[p + 1:] = nums[p + 1:][::-1]


if __name__ == '__main__':
    Solution().nextPermutation([3, 2, 1])
