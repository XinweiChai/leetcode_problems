from typing import List


class Solution(object):
    def longestConsecutive(self, nums: List[int]) -> int:
        # # Sort O(nlogn)
        # if not nums:
        #     return 0
        # nums.sort()
        # longest = 1
        # count = 1
        # for i in range(len(nums) - 1):
        #     if nums[i] + 1 == nums[i + 1]:
        #         count += 1
        #         longest = max(longest, count)
        #     elif nums[i] != nums[i + 1]:
        #         count = 1
        # return longest

        # HashSet O(n)
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

print(Solution().longestConsecutive([1,2,0,1]))
