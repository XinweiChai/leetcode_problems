from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for _ in range(2):
            for idx, i in enumerate(nums):
                while stack and stack[-1][1] < i:
                    pos, _ = stack.pop()
                    res[pos] = i
                stack.append((idx, i))
        return res


if __name__ == '__main__':
    print(Solution().nextGreaterElements([1, 2, 1]))
