from python.TreeNode import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        tot = 0
        if root:
            if root.left:
                if root.left.left or root.left.right:
                    tot += self.sumOfLeftLeaves(root.left)
                else:
                    tot += root.left.val
            tot += self.sumOfLeftLeaves(root.right)
        return tot
