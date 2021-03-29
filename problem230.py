# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Inorder traversal
        # def rec(node):
        #     nonlocal k
        #     if node:
        #         l = rec(node.left)
        #         k -= 1
        #         if not k:
        #             return node.val
        #         if l is not None:
        #             return l
        #         r = rec(node.right)
        #         return r
        #
        # return rec(root)

        # Ver.2 fastest
        # def rec(node, cnt):
        #     if node:
        #         cnt, l = rec(node.left, cnt)
        #         cnt -= 1
        #         if not cnt:
        #             return cnt, node.val
        #         if l is not None:
        #             return cnt, l
        #         cnt, r = rec(node.right, cnt)
        #         return cnt, r
        #     return cnt, None
        #
        # return rec(root, k)[1]

        # Iterative
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


# print(Solution().kthSmallest(TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4)), 4))
print(Solution().kthSmallest(TreeNode(3, left=TreeNode(0, right=TreeNode(2, left=TreeNode(1)))), 4))
