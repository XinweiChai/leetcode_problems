from TreeNode import TreeNode, create_tree


# class BSTIterator:
#
#     def __init__(self, root: TreeNode):
#         self.stack = []
#         while root:
#             self.stack.append([root, False])
#             root = root.left
#
#     def next(self) -> int:
#         self.hasNext()
#         cur = self.stack[-1][0]
#         temp = cur.val
#         self.stack[-1][1] = True
#         if cur.right:
#             cur = cur.right
#             self.stack.append([cur, False])
#             while cur.left:
#                 cur = cur.left
#                 self.stack.append([cur, False])
#         return temp
#
#     def hasNext(self) -> bool:
#         while self.stack:
#             cur, state = self.stack[-1]
#             if state:
#                 self.stack.pop()
#             else:
#                 return True
#         return False

# A more efficient implementation
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root_node = root
        self.current_node = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current_node is not None or len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        while self.current_node:
            self.stack.append(self.current_node)
            self.current_node = self.current_node.left
        next = self.stack.pop()
        self.current_node = next.right
        return next.val


if __name__ == '__main__':
    # Your BSTIterator object will be instantiated and called as such:
    tree = create_tree(TreeNode, [[1], [2, 3], [4, 5, 6, 7]])
    obj = BSTIterator(tree)
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
