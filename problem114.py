# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # def __init__(self):
    #     self.cur = None
    #
    # def flatten(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #
    #     if root:
    #         root.right, root.left = root.left, root.right
    #         if root.right:
    #             self.flatten(root.right)
    #         else:
    #             self.cur = root
    #         if root.left:
    #             self.cur.right = root.left
    #             root.left = None
    #             self.flatten(self.cur.right)

    # A more clever solution
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


Solution().flatten(
    TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(5, right=TreeNode(6))))
