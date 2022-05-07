from typing import Sequence


class Solution:
    # s_2 > s_3 > s_1
    def find132pattern(self, nums: Sequence[int]) -> bool:
        stack = []
        s3 = float('-inf')
        for n in nums[::-1]:
            if n < s3:
                return True
            # We find s_3 which means at least one number is larger than s_3
            # s_2 is the top of stack
            while stack and n > stack[-1]:
                s3 = stack.pop()
            stack.append(n)
        return False

    # Using O(1) space, make use of the original list as a stack
    def find132pattern2(self, nums: Sequence[int]) -> bool:
        n = top = len(nums)
        third = float('-inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < third:
                return True
            while top < n and nums[i] > nums[top]:
                third = nums[top]
                top += 1
            top -= 1
            nums[top] = nums[i]
        return False


if __name__ == '__main__':
    print(Solution().find132pattern2([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 1]))
