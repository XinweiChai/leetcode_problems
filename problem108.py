# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            l = len(nums) // 2
            root = TreeNode(nums[l])
            root.left = self.sortedArrayToBST(nums[:l])
            root.right = self.sortedArrayToBST(nums[l + 1:])
            return root
