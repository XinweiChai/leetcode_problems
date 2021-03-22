# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def rec(node1, node2):
            if node1 and node2:
                node1.val += node2.val
                node1.left = rec(node1.left, node2.left)
                node1.right = rec(node1.right, node2.right)
                return node1
            else:
                return node1 or node2

        return rec(root1, root2)
