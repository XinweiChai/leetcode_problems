# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # res = None
        #
        # def rec(node):
        #     nonlocal res
        #     if node:
        #         l = rec(node.left)
        #         r = rec(node.right)
        #         cur = 1 if node == p or node == q else 0
        #         if l + r + cur == 2:
        #             res = node
        #         return l or r or cur
        #     else:
        #         return 0
        # rec(root)
        # return res

        # A more clever way
        if root is None:
            return None

        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        if (left_res and right_res) or (root in [p, q]):
            return root
        else:
            return left_res or right_res
