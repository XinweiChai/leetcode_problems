# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # if not root:
        #     return []
        # cur = [root]
        # view = []
        # while cur:
        #     view.append(cur[-1].val)
        #     temp = []
        #     for i in cur:
        #         if i.left:
        #             temp.append(i.left)
        #         if i.right:
        #             temp.append(i.right)
        #     cur = temp
        # return view

        # Recursion
        view = []

        def rec(node, level):
            if node:
                if len(view) < level:
                    view.append(node.val)
                rec(node.right, level + 1)
                rec(node.left, level + 1)

        rec(root, 1)
        return view
