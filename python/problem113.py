from TreeNode import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> Sequence[Sequence[int]]:
        if not root:
            return []
        paths = []
        cur = []

        def rec(node, total):
            cur.append(node.val)
            if not node.left and not node.right:
                if total - node.val == 0:
                    paths.append(cur.copy())
            if node.left:
                rec(node.left, total - node.val)
            if node.right:
                rec(node.right, total - node.val)
            cur.pop()

        rec(root, targetSum)
        return paths