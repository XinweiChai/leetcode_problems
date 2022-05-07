from typing import Sequence

from TreeNode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) ->Sequence[Sequence[int]]:
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
