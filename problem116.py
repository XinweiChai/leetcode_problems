"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        # def rec(nodes):
        #     if nodes[0]:
        #         new_nodes = []
        #         for i in range(len(nodes)):
        #             if i != len(nodes) - 1:
        #                 nodes[i].next = nodes[i + 1]
        #             new_nodes.append(nodes[i].left)
        #             new_nodes.append(nodes[i].right)
        #         rec(new_nodes)
        #
        # rec([root])
        # return root

        # Using O(1) space
        level_start = root
        while level_start:
            cur = level_start
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            level_start = level_start.left
        return root
