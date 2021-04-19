from typing import List
from TreeNode import TreeNode


class Solution(object):
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        cur = [root]
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
            if temp:
                ans.append(temp)
        return ans
