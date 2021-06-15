from python.TreeNode import TreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = 0

        def rec(node):
            nonlocal res
            if not node:
                return 0
            sum_left = rec(node.left)
            sum_right = rec(node.right)
            res += abs(sum_left - sum_right)
            return sum_left + sum_right + node.val

        rec(root)
        return res
