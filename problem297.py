from TreeNode import TreeNode


# class Codec:
#
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype -> str
#         """
#         s = []
#         cur = [root]
#         while cur:
#             empty = True
#             sub = []
#             for i in cur:
#                 if i:
#                     empty = False
#                     sub.append(str(i.val))
#                 else:
#                     sub.append('None')
#             if not empty:
#                 s.append(','.join(sub))
#             temp = []
#             for i in cur:
#                 if i:
#                     temp.append(i.left)
#                     temp.append(i.right)
#             cur = temp
#         return ';'.join(s)
#
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#
#         :type data: str
#         :rtype -> TreeNode
#         """
#         if not data:
#             return None
#         s = data.split(';')
#         sentinel = TreeNode(0)
#         head = sentinel
#         cur = [head]
#         for i in s:
#             sub = i.split(',')
#             temp = []
#             left = True
#             pos = 0
#             for j in sub:
#                 if j != 'None':
#                     node = TreeNode(int(j))
#                     temp.append(node)
#                 else:
#                     node = None
#                 if left:
#                     cur[pos].left = node
#                 else:
#                     cur[pos].right = node
#                     pos += 1
#                 left = not left
#             cur = temp
#         return sentinel.left

# Concise version
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.left = b
a.right = c
c.left = TreeNode(4)
c.right = TreeNode(5)

ser = Codec()
deser = Codec()
y = deser.deserialize(ser.serialize(a))
