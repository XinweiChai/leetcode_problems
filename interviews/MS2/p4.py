# Leetcode 1022
"""
1. You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

             1
        0        1
    0      1   0    1

"""
from python.TreeNode import TreeNode


def sum_tree(root: TreeNode) -> int:
    if not root:
        return 0
    tot = 0

    def rec(node, cur):
        nonlocal tot
        if not node.left and not node.right:
            tot += cur * 2 + node.val
        else:
            if node.left:
                rec(node.left, cur * 2 + node.val)
            if node.right:
                rec(node.right, cur * 2 + node.val)

    rec(root, 0)
    return tot


def sum_tree2(root: TreeNode) -> int:
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
def sum_tree3(root: TreeNode) -> int:
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
