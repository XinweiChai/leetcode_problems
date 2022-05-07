from typing import Sequence
from TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: Sequence[int]) -> TreeNode:
        if nums:
            l = len(nums) // 2
            root = TreeNode(nums[l])
            root.left = self.sortedArrayToBST(nums[:l])
            root.right = self.sortedArrayToBST(nums[l + 1:])
            return root
