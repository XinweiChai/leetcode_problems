import collections

from python.TreeNode import TreeNode, create_tree


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # vals = collections.deque(int(val) for val in data.split())
        vals = [int(val) for val in data.split()]
        ptr = 0

        def build(minVal, maxVal):
            nonlocal ptr
            # if vals and minVal < vals[0] < maxVal:
            if ptr < len(vals) and minVal < vals[ptr] < maxVal:
                val = vals[ptr]
                # val = vals.popleft()
                ptr += 1
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()
    tree = ser.serialize(create_tree([[2], [None, 3]]))
    ans = deser.deserialize(tree)
    ans.print_all()
