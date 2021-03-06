# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        cur = [root]
        count = 0
        while cur:
            swap = []
            temp = []
            for i in cur:
                temp.append(i.val)
                if i.left:
                    swap.append(i.left)
                if i.right:
                    swap.append(i.right)
            cur = swap
            if count:
                temp.reverse()
            if temp:
                ans.append(temp)
            count = 1 - count
        return ans
