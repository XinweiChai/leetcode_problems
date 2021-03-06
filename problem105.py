# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # ans = []
        #
        # def rec(pre, ino):
        #     if pre:
        #         head = pre[0]
        #         ans.append(head)
        #         ind = ino.index(head)
        #         rec(pre[1:ind+1], ino[:ind])
        #         rec(pre[ind+1:], ino[ind+1:])
        #
        # rec(preorder,inorder)

        # Concise version but takes time and space
        # if inorder:
        #     ind = inorder.index(preorder.pop(0))
        #     root = TreeNode(inorder[ind])
        #     root.left = self.buildTree(preorder, inorder[0:ind])
        #     root.right = self.buildTree(preorder, inorder[ind + 1:])
        #     return root

        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i

        def recur(low, high):
            if low > high: return None
            x = TreeNode(preorder.pop(0))
            mid = map_inorder[x.val]
            x.left = recur(low, mid - 1)
            x.right = recur(mid + 1, high)
            return x

        return recur(0, len(inorder) - 1)
