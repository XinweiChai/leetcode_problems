# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return []

        def rec(nodes):
            if nodes:
                new_nodes = []
                for i in nodes:
                    if i:
                        if i.left:
                            new_nodes.append(i.left)
                        if i.right:
                            new_nodes.append(i.right)
                rec(new_nodes)
                ans.append([i.val for i in nodes if i])

        rec([root])
        return ans
