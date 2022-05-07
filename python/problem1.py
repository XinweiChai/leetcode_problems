from typing import Sequence


class Solution:
    def twoSum(self, nums: Sequence[int], target: int) -> Sequence[int]:
        # Worse solution, sort and search O(nlogn)
        # nums = list(enumerate(nums))
        # nums.sort(key=lambda x: x[1])
        # left = 0
        # right = len(nums) - 1
        # while left != right:
        #     if nums[left][1] + nums[right][1] < target:
        #         left += 1
        #     elif nums[left][1] + nums[right][1] > target:
        #         right -= 1
        #     else:
        #         return [nums[left][0], nums[right][0]]

        # Using Hashtable, O(n)
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

if __name__ == '__main__':
    print(Solution().twoSum([-3, 4, 3, 90], 0))
