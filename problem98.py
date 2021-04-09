from TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def rec(node, inf, sup):
            if not node:
                return True
            if node.val <= inf or node.val >= sup:
                return False
            if not rec(node.left, inf, node.val):
                return False
            if not rec(node.right, node.val, sup):
                return False
            return True

        return rec(root, -float('inf'), float('inf'))


print(Solution().isValidBST(TreeNode(5, left=TreeNode(4), right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))))
