from collections import deque
from typing import Optional
from TreeNode import TreeNode, create_tree


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        q = deque([root])
        l = 1
        for _ in range(depth - 2):
            cnt = 0
            for i in range(l):
                cur = q.popleft()
                if cur.left:
                    cnt += 1
                    q.append(cur.left)
                if cur.right:
                    cnt += 1
                    q.append(cur.right)
            l = cnt
        for i in q:
            i.left = TreeNode(val, left=i.left)
            i.right = TreeNode(val, right=i.right)
        return root


if __name__ == '__main__':
    print(Solution().addOneRow(create_tree([1, 2, 3, 4]), 5, 4))
