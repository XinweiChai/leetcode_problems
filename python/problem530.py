from python.TreeNode import TreeNode, create_tree


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_dif = float('inf')
        last = -float('inf')

        def inorder(node):
            nonlocal min_dif
            nonlocal last
            if node:
                inorder(node.left)
                min_dif = min(min_dif, node.val - last)
                last = node.val
                inorder(node.right)

        inorder(root)
        return min_dif


if __name__ == '__main__':
    print(Solution().getMinimumDifference(create_tree([[4], [2, 6], [1, 3, None, None]])))
