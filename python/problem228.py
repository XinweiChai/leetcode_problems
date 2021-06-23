from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start = 0
        while start < len(nums):
            end = start
            while end < len(nums) and nums[end] - nums[start] == end-start:
                end += 1
            end -= 1
            if start == end:
                res.append(str(nums[start]))
            else:
                res.append(str(nums[start]) + '->' + str(nums[end]))
            start = end + 1

        return res


if __name__ == '__main__':
    print(Solution().summaryRanges([0,1,2,4,5,7]))