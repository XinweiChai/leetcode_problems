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
    sum = 0

    def rec(node, cur):
        if not node.left and not node.right:
            sum += cur * 2 + node.val
        else:
            if node.left:
                rec(node.left, cur * 2 + node.val)
            if node.right:
                rec(node.right, cur * 2 + node.val)

    rec(root, 0)
    return sum


def sum_tree2(root: TreeNode) -> int:
    if not root:
        return 0
    to_visit = []
    sum = 0
    cur = 0
    while root:
        if root.right:
            to_visit.append((root.right, to_visit[-1][1] * 2 + to_visit[-1][0].right.val))
        if root.left:
            cur = 2 * cur + root.val
        else:
            root, val = to_visit.pop()
