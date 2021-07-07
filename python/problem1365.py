from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n
        # nums = sorted(enumerate(nums), key=lambda x: x[1])
        # for i in range(n):
        #     if i and nums[i][1] != nums[i - 1][1]:
        #         res[nums[i][0]] = i
        #     else:
        #         res[nums[i][0]] = res[nums[i - 1][0]]
        # return res

        count = [0] * 102
        for num in nums:
            count[num + 1] += 1
        for i in range(1, 102):
            count[i] += count[i - 1]
        return [count[num] for num in nums]


if __name__ == '__main__':
    print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
