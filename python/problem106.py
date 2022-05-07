from TreeNode import TreeNode
from typing import Sequence


class Solution:
    def buildTree(self, inorder: Sequence[int], postorder: Sequence[int]) -> TreeNode:
        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        def recur(low, high):
            if low > high:
                return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid + 1, high)
            x.left = recur(low, mid - 1)
            return x

        return recur(0, len(inorder) - 1)
