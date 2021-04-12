from TreeNode import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        def rec(node, total):
            if not node.left and not node.right:
                return total - node.val == 0
            return (node.left and rec(node.left, total - node.val)) or (
                        node.right and rec(node.right, total - node.val))

        return rec(root, targetSum)
