from collections import Counter


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = Counter(nums)
        res = [[]]
        for i in nums:
            l = len(res)
            temp = []
            for k in range(nums[i]):
                temp.append(i)
                for j in range(l):
                    res.append(res[j] + temp)
        return res


print(Solution().subsetsWithDup([1, 2, 2]))
