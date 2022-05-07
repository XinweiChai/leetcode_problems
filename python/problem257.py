from typing import Sequence

from python.TreeNode import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> Sequence[str]:
        res = []
        def rec(node, cur):
            if not node.left and not node.right:
                res.append(cur + str(node.val))
            else:
                if node.left:
                    rec(node.left, cur + str(node.val) + "->")
                if node.right:
                    rec(node.right, cur + str(node.val) + "->")
        rec(root, "")
        return res