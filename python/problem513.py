import collections

from python import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        ans = []
        q = collections.deque([root])
        while q:
            c = len(q)
            ans.append(q[0].val)
            while c:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                c -= 1
        return ans[-1]
