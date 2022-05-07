from typing import Sequence
import heapq


class Solution:
    def findUnsortedSubarray(self, nums: Sequence[int]) -> int:
        # O(nlogn)
        # aux = sorted(nums)
        # l = 0
        # r = len(nums) - 1
        # while l <= r and aux[l] == nums[l]:
        #     l += 1
        # while l <= r and aux[r] == nums[r]:
        #     r -= 1
        # return r - l + 1

        # Using heap O(nlogn)
        # left = 0
        # right = len(nums) - 1
        # aux = nums.copy()
        # heapq.heapify(aux)
        # for i in range(len(nums)):
        #     if nums[i] != heapq.heappop(aux):
        #         break
        #     left += 1
        # aux = [-i for i in nums]
        # heapq.heapify(aux)
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] != - heapq.heappop(aux) or right <= left:
        #         break
        #     right -= 1
        # return right - left + 1

        # Using stack O(n)
        # stack = []
        # l = len(nums)
        # r = 0
        # for i in range(len(nums)):
        #     while stack and nums[i] < nums[stack[-1]]:
        #         l = min(l, stack.pop())
        #     stack.append(i)
        #
        # stack.clear()
        # for i in range(len(nums) - 1, -1, -1):
        #     while stack and nums[i] > nums[stack[-1]]:
        #         r = max(r, stack.pop())
        #     stack.append(i)
        # return max(0, r - l + 1)

        # Without stack
        left, right = 0, len(nums) - 1
        min_val, max_val = float('inf'), float('-inf')
        start, end = 0, -1
        while right >= 0:
            if nums[left] >= max_val:
                max_val = nums[left]
            else:
                end = left
            if nums[right] <= min_val:
                min_val = nums[right]
            else:
                start = right
            left += 1
            right -= 1

        return end - start + 1


print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(Solution().findUnsortedSubarray([1, 2, 3, 4]))
print(Solution().findUnsortedSubarray([1, 3, 5, 4, 2]))
