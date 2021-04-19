from TreeNode import TreeNode, create_tree


class Solution:

    # def __init__(self):
    #     self.cur = None
    #
    # def flatten(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #
    #     if root:
    #         root.right, root.left = root.left, root.right
    #         if root.right:
    #             self.flatten(root.right)
    #         else:
    #             self.cur = root
    #         if root.left:
    #             self.cur.right = root.left
    #             root.left = None
    #             self.flatten(self.cur.right)

    # A more clever solution
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
        return root


x = create_tree([[1], [2, 5], [3, 4, None, 6]])
Solution().flatten(x)
x.print_all()