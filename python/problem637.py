from typing import List

from python.TreeNode import TreeNode
from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            tot = 0
            cnt = 0
            for _ in range(size):
                temp = q.popleft()
                tot += temp.val
                cnt += 1
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            res.append(tot / cnt)
        return res
