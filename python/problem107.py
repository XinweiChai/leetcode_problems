from typing import Sequence
from TreeNode import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> Sequence[Sequence[int]]:
        ans = []
        if not root:
            return []

        def rec(nodes):
            if nodes:
                new_nodes = []
                for i in nodes:
                    if i:
                        if i.left:
                            new_nodes.append(i.left)
                        if i.right:
                            new_nodes.append(i.right)
                rec(new_nodes)
                ans.append([i.val for i in nodes if i])

        rec([root])
        return ans
