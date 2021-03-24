# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Copy takes much extra space
        # cnt = 0
        #
        # def rec(node, sums):
        #     nonlocal cnt
        #     if node:
        #         if node.val == sum:
        #             cnt += 1
        #         for i in range(len(sums)):
        #             sums[i] += node.val
        #             if sums[i] == sum:
        #                 cnt += 1
        #         sums.append(node.val)
        #         rec(node.left, sums.copy())
        #         rec(node.right, sums)
        # rec(root, [])
        # return cnt

        # Using Hashmap and avoiding copy
        def rec(node, total, sums):
            nonlocal cnt
            if node:
                total += node.val
                if total - sum in sums:
                    cnt += sums[total - sum]
                sums[total] = sums[total] + 1 if total in sums else 1
                rec(node.left, total, sums)
                rec(node.right, total, sums)
                sums[total] -= 1
                if sums[total] == 0:
                    sums.pop(total)

        cnt = 0
        rec(root, 0, {0: 1})
        return cnt


print(Solution().pathSum(TreeNode(10, left=TreeNode(5, left=TreeNode(3, left=TreeNode(3), right=TreeNode(-2)),
                                                    right=TreeNode(2, right=TreeNode(1))),
                                  right=TreeNode(-3, right=TreeNode(11))), 8))
