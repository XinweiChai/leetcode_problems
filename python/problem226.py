from TreeNode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # def rec(node):
        #     if node:
        #         rec(node.left)
        #         rec(node.right)
        #         node.left, node.right = node.right, node.left
        # rec(root)
        # return root
        if not root:
            return None
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        return root
