from typing import List
import random


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
        def nth_element(start, end, n):
            low = -1
            while low != n:
                pivot = random.randrange(start, end)
                nums[pivot], nums[end - 1] = nums[end - 1], nums[pivot]
                low = start
                for i in range(start, end - 1):
                    if nums[end - 1] > nums[i]:
                        nums[i], nums[low] = nums[low], nums[i]
                        low += 1
                nums[end - 1], nums[low] = nums[low], nums[end - 1]
                if low < n:
                    start = low + 1
                elif low > n:
                    end = low

        nth_element(0, len(nums), len(nums) // 2)
        mid = nums[len(nums) // 2]

        def new_index(x):
            return (1 + 2 * x) % (len(nums) | 1)
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[new_index(j)] > mid:
                nums[new_index(i)], nums[new_index(j)] = nums[new_index(j)], nums[new_index(i)]
                i += 1
                j += 1
            elif nums[new_index(j)] < mid:
                nums[new_index(j)], nums[new_index(k)] = nums[new_index(k)], nums[new_index(j)]
                k -= 1
            else:
                j += 1


# print(Solution().wiggleSort([1, 5, 1, 1, 6, 4]))
# print(Solution().wiggleSort([1, 3, 2, 2, 3, 1]))
print(Solution().wiggleSort([5, 4, 10, 2, 3, 6, 1, 7, 9, 8]))
