from TreeNode import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # Recursion
        # if not root:
        #     return 0
        # l = self.minDepth(root.left)
        # if l==1:
        #     return 2
        # r = self.minDepth(root.right)
        # if l and r:
        #     return min(l, r)+1
        # return (l or r) + 1

        # BFS, fastest
        if not root:
            return 0
        cur = [root]
        depth = 1
        while cur:
            temp = []
            for i in cur:
                if not i.left and not i.right:
                    return depth
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            cur = temp
            depth += 1
