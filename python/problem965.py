from python.TreeNode import TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val

        def rec(node):
            if node:
                return node.val == val and rec(node.left) and rec(node.right)
            return True

        return rec(root)
