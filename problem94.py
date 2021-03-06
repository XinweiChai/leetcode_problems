# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
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