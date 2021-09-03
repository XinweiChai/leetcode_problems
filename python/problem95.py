from TreeNode import TreeNode
from typing import List


class Solution:
    # def generateTrees(self, n: int) -> List[TreeNode]:
    #     cand = list(range(1, 1 + n))
    #
    #     def fill_tree(nums):
    #         if not nums:
    #             return [None]
    #         res = []
    #         for i in range(len(nums)):
    #             for j in fill_tree(nums[:i]):
    #                 for k in fill_tree(nums[i + 1:]):
    #                     res.append(TreeNode(nums[i], j, k))
    #         return res
    #
    #     return fill_tree(cand)

    # With memo
    def generateTrees(self, n: int) -> List[TreeNode]:
        cand = list(range(1, 1 + n))
        memo = {}

        def fill_tree(l, r):
            if l == r:
                return [None]
            res = []
            if (l, r) in memo:
                return memo[l, r]
            for i in range(l, r):
                for j in fill_tree(l, i):
                    for k in fill_tree(i + 1, r):
                        res.append(TreeNode(cand[i], j, k))
            memo[l, r] = res
            return res

        return fill_tree(0, len(cand))


Solution().generateTrees(3)