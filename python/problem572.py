from python.TreeNode import TreeNode, create_tree
from hashlib import sha256


class MerkleTree(TreeNode):
    def __init__(self, val=0, left=None, right=None):
        super().__init__(val, left, right)
        # Equivalent to
        # TreeNode.__init__(self, val, left, right)
        self.merkle = None


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def is_identical(r1, r2):
            if not r1 or not r2:
                return r1 is r2
            return r1.val == r2.val and is_identical(r1.left, r2.left) and is_identical(r1.right, r2.right)

        if not root:
            return False
        if is_identical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtree2(self, s: MerkleTree, t: MerkleTree):
        def hash_(x):
            S = sha256()
            S.update(x.encode('utf-8'))
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            # node.merkle = hash_(m_left + str(node.val) + m_right)
            node.merkle = hash(str(m_left) + str(node.val) + str(m_right))
            return node.merkle

        merkle(s)
        merkle(t)

        def dfs(node):
            if not node:
                return False
            return (node.merkle == t.merkle or
                    dfs(node.left) or dfs(node.right))

        return dfs(s)


if __name__ == '__main__':
    root = create_tree([[3], [4, 5], [1, 2, None, None]], MerkleTree)
    subRoot = create_tree([[4], [1, 2]], MerkleTree)
    print(Solution().isSubtree2(root, subRoot))
