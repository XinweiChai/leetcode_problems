from typing import List


from TreeNode import TreeNode


class Solution(object):
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # Concise version but takes time and space
        # if inorder:
        #     ind = inorder.index(preorder.pop(0))
        #     root = TreeNode(inorder[ind])
        #     root.left = self.buildTree(preorder, inorder[0:ind])
        #     root.right = self.buildTree(preorder, inorder[ind + 1:])
        #     return root

        # cnt = 0
        #
        # def rec(start_idx, end_idx):
        #     nonlocal cnt
        #     if end_idx > start_idx:
        #         idx = inorder.index(preorder[cnt])
        #         cnt += 1
        #         root = TreeNode(inorder[idx])
        #         root.left = rec(start_idx, idx)
        #         root.right = rec(idx + 1, end_idx)
        #         return root
        #
        # return rec(0, len(inorder))

        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        preorder.reverse()

        def recur(low, high):
            if low <= high:
                x = TreeNode(preorder.pop())
                mid = map_inorder[x.val]
                x.left = recur(low, mid - 1)
                x.right = recur(mid + 1, high)
                return x

        return recur(0, len(inorder) - 1)


x = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
x.print_all()
