from python.TreeNode import TreeNode, create_tree


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ptr = root
        depth = 0
        while ptr.left:
            depth += 1
            ptr = ptr.left
        cnt = 2 ** depth - 1

        def has_mid(node, dep):
            node = node.left
            for _ in range(dep):
                node = node.right
            return bool(node)

        def rec(node, dep):
            nonlocal cnt
            while dep:
                dep -= 1
                if has_mid(node, dep):
                    cnt += 2 ** dep
                    node = node.right
                else:
                    node = node.left
            if node:
                cnt += 1

        rec(root, depth)
        return cnt


if __name__ == '__main__':
    print(Solution().countNodes(create_tree([[1], [2, 3], [4, 5, None, None]])))
