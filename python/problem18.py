from typing import List


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
#             res = []
#             if len(nums) < k or nums[0] * k > target or target > nums[-1] * k:
#                 return res
#             if k == 2:
#                 return twoSum(nums, target)
#             for i in range(len(nums) - k + 1):
#                 if i == 0 or nums[i - 1] != nums[i]:
#                     for j in kSum(nums[i + 1:], target - nums[i], k - 1):
#                         res.append(j + [nums[i]])
#             return res
#
#         def twoSum(nums: List[int], target: int) -> List[List[int]]:
#             res = []
#             lo, hi = 0, len(nums) - 1
#             while lo < hi:
#                 total = nums[lo] + nums[hi]
#                 if total < target or (lo > 0 and nums[lo] == nums[lo - 1]):
#                     lo += 1
#                 elif total > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
#                     hi -= 1
#                 else:
#                     res.append([nums[lo], nums[hi]])
#                     lo += 1
#                     hi -= 1
#             return res
#
#         nums.sort()
#         return kSum(nums, target, 4)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            if k == 2:
                return twoSum(nums, target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for set in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return res

        nums.sort()
        return kSum(nums, target, 4)
print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
