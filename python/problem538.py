from typing import Optional
from TreeNode import TreeNode, create_tree


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # acc is the accumulate sum of the seen nodes, troublesome
        def rec(node, acc):
            if not node:
                return 0
            right = rec(node.right, acc)
            node.val += right + acc
            left = rec(node.left, node.val)
            return node.val + left - acc

        rec(root, 0)
        return root

    def convertBST2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tot = 0

        def rec(node):
            if node:
                nonlocal tot
                rec(node.right)
                tot += node.val
                node.val = tot
                rec(node.left)

        rec(root)
        return root


if __name__ == '__main__':
    print(Solution().convertBST(create_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])))
