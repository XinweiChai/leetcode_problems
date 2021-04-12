from TreeNode import TreeNode


class Solution:
    def isBalanced(self, root):

        def check(node):
            if node is None:
                return 0
            left = check(node.left)
            right = check(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1
