import TreeNode
from collections import deque


def level_order(root: TreeNode):
    cur = deque()
    cur.append(root)
    while len(cur):
        x = cur.pop()
        yield x.val
        if x.left:
            cur.append(x.left)
        if x.right:
            cur.append(x.right)


def pre_order(root: TreeNode):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)


# Put left branch to stack, recommended
def pre_order_iterative(root: TreeNode):
    s = []
    while s or root:
        if root:
            yield root.val
            s.append(root)
            root = root.left
        else:
            root = s.pop()
            root = root.right


# Put right branch to stack
def pre_order_iterative2(root: TreeNode):
    stack = [root]
    while stack:
        if root:
            yield root.val
            if root.right:
                stack.append(root.right)
            root = root.left
        else:
            root = stack.pop()


def in_order(root: TreeNode):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


def in_order_iterative(root: TreeNode):
    s = []
    while s or root:
        if root:
            s.append(root)
            root = root.left
        else:
            root = s.pop()
            yield root.val
            root = root.right


def post_order(root: TreeNode):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)


# The problem with post-order traversal is that in the previous two cases
# when a node was popped of from the stack,
# then it was finally removed and was not accessed again.
# However in case of post-order the node needs to be accessed from the stack twice,
# and is deleted only in the second access.
# First time we find a node, we push it on to the stack,
# the second time we examine it from the stack to go to it's right child
# and then finally after visiting both the right sub-tree and the left-subtree,
# we remove the node from the stack.
# So a node stays in the stack as long as it's sub-trees have not been visited.
# Variable last_visited is to mark if the right branch has been traversed.
def post_order_iterative(root: TreeNode):
    s = []
    last_visited = None
    while s or root:
        if root:
            s.append(root)
            root = root.left
        else:
            top = s[-1]
            if top.right and last_visited != top.right:
                root = top.right
            else:
                yield top.val
                last_visited = s.pop()


# Avoid stack occupying extra space
def morris_traversal(root: TreeNode) -> None:
    while root:
        if not root.left:
            print(root.val)
            root = root.right
        else:
            pred = root.left
            while pred.right and pred.right != root:
                pred = pred.right
            if not pred.right:
                # print(root.val)  # Preorder
                pred.right = root
                root = root.left
            else:
                print(root.val)  # Inorder
                pred.right = None
                root = root.right


def morris_traversal_post_order(root: TreeNode) -> None:
    if not root:
        return
    current = TreeNode.TreeNode(-1)
    current.left = root
    while current:
        # If left child is None.
        # Move to right child.
        if not current.left:
            current = current.right
        else:
            pre = current.left
            # Inorder predecessor
            while pre.right and pre.right != current:
                pre = pre.right
            # The connection between current
            # and predecessor is made
            if not pre.right:
                # Make current as the right
                # child of the right most node
                pre.right = current
                # Traverse the left child
                current = current.left
            else:
                pre.right = None
                succ = current
                current = current.left
                prev = None
                # Traverse along the right
                # subtree to the
                # right-most child
                while current:
                    temp = current.right
                    current.right = prev
                    prev = current
                    current = temp
                # Traverse back
                # to current's left child
                # node
                while prev:
                    print(prev.val, end=' ')
                    temp = prev.right
                    prev.right = current
                    current = prev
                    prev = temp
                current = succ
                current = current.right


if __name__ == '__main__':
    tree = TreeNode.create_tree([[1], [2, 3], [4, 5, 6, 7]])
    # for i in level_order(tree):
    #     print(i)

    # in_order(tree)
    # for i in in_order_iterative(tree):
    #     print(i)

    # pre_order(tree)
    # for i in pre_order_iterative(tree):
    #     print(i)

    # post_order(tree)
    # for i in post_order_iterative(tree):
    #     print(i)
    # morris_traversal(tree)
    morris_traversal_post_order(tree)