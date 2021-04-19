from TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_val = -float('inf')

        def rec(node):
            nonlocal max_val
            if not node:
                return 0
            l = max(0, rec(node.left))
            r = max(0, rec(node.right))
            cur_max = l + r + node.val
            max_val = max(max_val, cur_max)
            return node.val + max(l, r)

        rec(root)
        return max_val
