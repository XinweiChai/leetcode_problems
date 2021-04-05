# Binary tree, return root-to-leaf paths whose sum equals to n

def find_path(root, n):
    if not root:
        return []
    paths = []
    cur = []

    def rec(node, total):
        cur.append(node)
        if not node.left and not node.right:
            if total - node.val == 0:
                paths.append(cur)
        if node.left:
            rec(node.left, total - node.val)
        if node.right:
            rec(node.right, total - node.val)
        cur.pop()

    rec(root, n)
    return paths


def find_path2(root, n):
    paths = []
    cur = []

    def rec(node, total):
        if not node:
            if total == 0:
                paths.append(cur)
        else:
            cur.append(node)
            rec(node.left, total - node.val)
            rec(node.right, total - node.val)
            cur.pop()

    rec(root, n)
    return paths
