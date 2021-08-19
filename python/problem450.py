# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from TreeNode import TreeNode, create_tree


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        sentinel = TreeNode(float('inf'), left=root)

        def find(node, pred, val):
            if not node:
                return None, pred
            if val == node.val:
                return node, pred
            elif val < node.val:
                return find(node.left, node, val)
            else:
                return find(node.right, node, val)

        target, prev = find(root, sentinel, key)
        if not target:
            return root

        def rebalance(node, pred):
            if not node.left and not node.right:
                if target.val < prev.val:
                    pred.left = None
                else:
                    pred.right = None
            else:
                if node.left:
                    cur = node.left
                    if cur.right:
                        while cur.right:
                            predecessor = cur
                            cur = cur.right
                        predecessor.right = None
                        node.val = cur.val
                    else:
                        node.val = node.left.val
                        node.left = node.left.left
                else:
                    cur = node.right
                    if cur.left:
                        while cur.left:
                            predecessor = cur
                            cur = cur.left
                        predecessor.left = None
                        node.val = cur.val
                    else:
                        node.val = node.right.val
                        node.right = node.right.right

        rebalance(target, prev)
        return sentinel.left


if __name__ == '__main__':
    Solution().deleteNode(create_tree([[5], [3, 6], [2, 4, None, 7]]), 5).print_all()
