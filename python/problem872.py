from typing import Optional

import TreeNode


class Solution:

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaf(cur):
            if cur.left or cur.right:
                if cur.left:
                    yield from getLeaf(cur.left)
                if cur.right: 
                    yield from getLeaf(cur.right)
            else:
                yield cur.val

        return list(getLeaf(root1)) == list(getLeaf(root2))