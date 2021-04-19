from typing import Optional
from TreeNode import TreeNode, create_tree


class Solution:
    # def recoverTree(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     prev: Optional[TreeNode] = None
    #     first: Optional[TreeNode] = None
    #     second: Optional[TreeNode] = None
    #
    #     def rec(node: TreeNode):
    #         nonlocal prev, first, second
    #         if node:
    #             rec(node.left)
    #             if prev and prev.val > node.val:
    #                 second = node
    #                 if not first:
    #                     first = prev
    #                 else:
    #                     return
    #             prev = node
    #             rec(node.right)
    #
    #     rec(root)
    #     first.val, second.val = second.val, first.val


    # Using Morris traversal
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev: Optional[TreeNode] = None
        first: Optional[TreeNode] = None
        second: Optional[TreeNode] = None

        def find_swap():
            nonlocal prev, first, second
            if prev and prev.val > root.val:
                second = root
                if not first:
                    first = prev
            prev = root

        while root:
            if not root.left:
                find_swap()
                root = root.right
            else:
                pred = root.left
                while pred.right and pred.right != root:
                    pred = pred.right
                if not pred.right:
                    pred.right = root
                    root = root.left
                else:
                    pred.right = None
                    find_swap()
                    root = root.right
        first.val, second.val = second.val, first.val


Solution().recoverTree(create_tree([[1], [3, None], [None, 2, None, None]]))
