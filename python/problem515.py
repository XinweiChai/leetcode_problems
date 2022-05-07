import collections
from typing import Optional, Sequence

from TreeNode import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> Sequence[int]:
        if not root:
            return []
        q = collections.deque([root])
        res = []
        while q:
            c = len(q)
            max_val = float('-inf')
            for _ in range(c):
                cur = q.popleft()
                max_val = max(max_val, cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(max_val)
        return res
