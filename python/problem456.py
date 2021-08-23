from typing import List


class Solution:
    # s_2 > s_3 > s_1
    def find132pattern(self, nums: List[int]) -> bool:
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


if __name__ == '__main__':
    print(Solution().find132pattern([1, 3, 2, 4, 5, 6, 7, 8, 9, 10]))
