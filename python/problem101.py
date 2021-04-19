from TreeNode import TreeNode


class Solution(object):
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True

        def rec(l_node, r_node):
            if not l_node:
                return not r_node
            if not r_node:
                return not l_node
            if l_node.val != r_node.val:
                return False
            return rec(l_node.left, r_node.right) and rec(l_node.right, r_node.left)

        return rec(root.left, root.right)
