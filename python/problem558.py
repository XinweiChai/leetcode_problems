# """
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# """

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:  # case 1: both are leaf nodes
            return Node(quadTree1.val | quadTree2.val, 1, None, None, None, None)
        elif quadTree1.isLeaf and not quadTree2.isLeaf:  # case 2: node 1 is leaf node, node 2 is not
            node = Node(0, 0,
                        self.intersect(quadTree1, quadTree2.topLeft),
                        self.intersect(quadTree1, quadTree2.topRight),
                        self.intersect(quadTree1, quadTree2.bottomLeft),
                        self.intersect(quadTree1, quadTree2.bottomRight))
        elif not quadTree1.isLeaf and quadTree2.isLeaf:  # case 3: node 2 is leaf node, node 1 is not
            node = Node(0, 0,
                        self.intersect(quadTree1.topLeft, quadTree2),
                        self.intersect(quadTree1.topRight, quadTree2),
                        self.intersect(quadTree1.bottomLeft, quadTree2),
                        self.intersect(quadTree1.bottomRight, quadTree2))
        else:  # case 4: neither nodes are leaf
            node = Node(0, 0,
                        self.intersect(quadTree1.topLeft, quadTree2.topLeft),
                        self.intersect(quadTree1.topRight, quadTree2.topRight),
                        self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
                        self.intersect(quadTree1.bottomRight, quadTree2.bottomRight))

        if node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf \
                and node.bottomRight.isLeaf and node.topLeft.val == node.topRight.val \
                == node.bottomLeft.val == node.bottomRight.val:  # shrink quad nodes to one leaf node is values in 4 areas are the same
            return Node(node.topLeft.val, 1, None, None, None, None)
        return node

if __name__ == '__main__':
    x = Solution().intersect(Node(0, 1), Node(0, 1))
    y = 1
