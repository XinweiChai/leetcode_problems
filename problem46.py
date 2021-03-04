class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Loop
        # res = [[nums[0]]]
        # count = 1
        # while count < len(nums):
        #     res = [i for i in res for _ in range(count + 1)]
        #     for i in range(len(res)):
        #         res[i] = res[i][:i % (count+1)] + [nums[count]] + res[i][i % (count+1):]
        #     count += 1
        # return res

        # Recursion
        def perm(cur, nums):
            if not nums:
                res.append(cur)
            else:
                for i in range(len(nums)):
                    perm(cur + [nums[i]], nums[:i] + nums[i + 1:])

        res = []
        perm([], nums)
        return res


print(Solution().permute([1, 2, 3]))
# print(Solution().permute([5, 4, 6, 2]))
