# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        cnt = 0

        def rec(node, sums):
            nonlocal cnt
            if node:
                if node.val == sum:
                    cnt += 1
                for i in range(len(sums)):
                    sums[i] += node.val
                    if sums[i] == sum:
                        cnt += 1
                sums.append(node.val)
                rec(node.left, sums)
                rec(node.right, sums)

        rec(root, [])
        return cnt


print(Solution().pathSum(TreeNode(10, left=TreeNode(5, left=TreeNode(3, left=TreeNode(3), right=TreeNode(-2)),
                                                    right=TreeNode(2, right=TreeNode(1))),
                                  right=TreeNode(-3, right=TreeNode(11))), 8))
