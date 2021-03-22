# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def rec(node):
            nonlocal diameter
            if not node:
                return 0
            l = rec(node.left)
            r = rec(node.right)
            diameter = max(diameter, l + r)
            return max(l, r) + 1
        rec(root)
        return diameter


print(Solution().diameterOfBinaryTree(
    TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))))
