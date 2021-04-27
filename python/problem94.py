import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []

        def rec(root):
            if root.left:
                rec(root.left)
            l.append(root.val)
            if root.right:
                rec(root.right)

        if root:
            rec(root)
        return l
