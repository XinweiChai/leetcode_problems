import TreeNode


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0

        def rec(node, cur):
            nonlocal tot
            if not node.left and not node.right:
                tot += cur << 1 | node.val
            else:
                if node.left:
                    rec(node.left, cur << 1 | node.val)
                if node.right:
                    rec(node.right, cur << 1 | node.val)

        tot = 0
        rec(root, 0)
        return tot

    # Iterative version
    def sumRootToLeaf2(self, root: TreeNode) -> int:
        stack = []
        tot = 0
        cur = 0
        while stack or root:
            if root:
                cur = cur << 1 | root.val
                stack.append((root, cur))
                if not root.left and not root.right:
                    tot += cur
                root = root.left
            else:
                root, cur = stack.pop()
                root = root.right
        return tot

    # Morris traversal
    def sumRootToLeaf3(self, root: TreeNode) -> int:
        root_to_leaf = curr_number = 0

        while root:
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:
                # Predecessor node is one step to the left
                # and then to the right till you can.
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = (curr_number << 1) | root.val
                    predecessor.right = root
                    root = root.left
                    # Break the link predecessor.right = root
                # Once the link is broken,
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    curr_number >>= steps
                    predecessor.right = None
                    root = root.right

            # If there is no left child
            # then just go right.
            else:
                curr_number = (curr_number << 1) | root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right

        return root_to_leaf


if __name__ == '__main__':
    print(Solution().sumRootToLeaf3(TreeNode.create_tree([[1], [0, 1], [0, 1, 0, 1]])))
