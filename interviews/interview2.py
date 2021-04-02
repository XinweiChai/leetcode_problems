class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Size of biggest BST in a Binary Tree
def max_BST(node):
    def rec(node):
        if not node:
            return 0, True, None, None
        l, l_is_BST, inf_l, sup_l = rec(node.left)
        r, r_is_BST, inf_r, sup_r = rec(node.right)
        if inf_l is None:
            inf_l = node.val
            inf_r = node.val
        if sup_l is None:
            sup_l = node.val
            sup_r = node.val
        if l_is_BST and r_is_BST and sup_l <= node.val <= inf_r:
            return l + r + 1, True, inf_l, sup_r
        return max(l, r), False, 0, 0

    return rec(node)[0]


def max_BST2(node):
    def rec(node):
        if node.left:
            l, l_is_BST, inf_l, sup_l = rec(node.left)
        else:
            l, l_is_BST, inf_l, sup_l = 0, True, node.val, node.val
        if node.right:
            r, r_is_BST, inf_r, sup_r = rec(node.right)
        else:
            r, r_is_BST, inf_r, sup_r = 0, True, node.val, node.val
        if l_is_BST and r_is_BST and sup_l <= node.val <= inf_r:
            return l + r + 1, True, inf_l, sup_r
        return max(l, r), False, 0, 0

    return rec(node)[0] if node else 0


root = Tree(0, Tree(1), Tree(2, Tree(1), Tree(3)))
print(max_BST(root))
print(max_BST2(root))
