# Binary tree, return root-to-leaf paths whose sum equals to n (problem #113)
from TreeNode import TreeNode, create_tree


def find_path(root: TreeNode, n):
    if not root:
        return []
    paths = []
    cur = []

    def rec(node, total):
        cur.append(node.val)
        if not node.left and not node.right:
            if total - node.val == 0:
                paths.append(cur.copy())
        if node.left:
            rec(node.left, total - node.val)
        if node.right:
            rec(node.right, total - node.val)
        cur.pop()

    rec(root, n)
    return paths

# This approach doesn't work because paths gets 2 identical cur when reaching leaves
# def find_path2(root: TreeNode, n):
#     paths = []
#     cur = []
#
#     def rec(node, total):
#         if not node:
#             if total == 0:
#                 paths.append(cur.copy())
#         else:
#             cur.append(node.val)
#             rec(node.left, total - node.val)
#             rec(node.right, total - node.val)
#             cur.pop()
#
#     rec(root, n)
#     return paths


print(find_path(create_tree([[5], [4, 8], [11, None, 13, 4], [7, 2, None, None, None, None, 5, 1]]), 22))
