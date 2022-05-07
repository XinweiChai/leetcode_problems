from typing import Sequence


class Solution:
    def maxNumber(self, nums1: Sequence[int], nums2: Sequence[int], k: int) -> Sequence[int]:
        def prep(nums, k):
            if not k:
                return []
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]

        return max(merge(prep(nums1, i), prep(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))


if __name__ == '__main__':
    print(Solution().maxNumber([3, 8, 5, 3, 4], [8, 7, 3, 6, 8], 5))
