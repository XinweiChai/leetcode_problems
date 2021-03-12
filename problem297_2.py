# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = []
        if not root:
            return ''

        def rec(node):
            s.append(str(node.val))
            if node.left:
                rec(node.left)
            else:
                s.append('None')
            if node.right:
                rec(node.right)
            else:
                s.append('None')
        rec(root)
        return ','.join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        node = TreeNode(int(nodes[0]))
        root = node

        def fill(p, node):
            if p < len(nodes):
                if node:
                    if nodes[p] != 'None':
                        node.left = TreeNode(int(nodes[p]))
                    p = fill(p + 1, node.left)
                    if nodes[p] != 'None':
                        node.right = TreeNode(int(nodes[p]))
                    p = fill(p + 1, node.right)
            return p

        fill(1, node)
        return root


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
