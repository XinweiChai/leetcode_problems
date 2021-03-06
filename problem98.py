# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def rec(root, inf, sup):
            if not root:
                return True
            if root.val <= inf or root.val >= sup:
                return False
            if root.left and not rec(root.left, inf, min(sup, root.val)):
                return False
            if root.right and not rec(root.right, max(inf, root.val), sup):
                return False
            return True

        return rec(root, -float('inf'), float('inf'))


print(Solution().isValidBST(TreeNode(5, left=TreeNode(4), right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))))
