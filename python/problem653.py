from python.TreeNode import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        lst = []

        def inorder(root):
            if root:
                inorder(root.left)
                lst.append(root.val)
                inorder(root.right)

        inorder(root)
        l = 0
        r = len(lst) - 1
        while l < r:
            sum = lst[l] + lst[r]
            if sum == k:
                return True
            if sum < k:
                l += 1
            else:
                r -= 1
        return False
