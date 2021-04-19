from TreeNode import TreeNode, create_tree


# Definition for a Node.
class Node(TreeNode):
    def __init__(self, val: int = 0, left=None, right=None):
        super().__init__(val, left, right)
        self.next = None


class Solution:
    def connect(self, root: Node) -> Node:
        # With extra space O(n)
        # if not root:
        #     return None
        # cur = [root]
        # while cur:
        #     temp = []
        #     for i in cur:
        #         if i.left:
        #             temp.append(i.left)
        #         if i.right:
        #             temp.append(i.right)
        #     for i in range(len(temp) - 1):
        #         temp[i].next = temp[i + 1]
        #     cur = temp
        # return root

        # Without extra space
        # saveroot = root
        # while root:
        #     cur = root
        #     to_point = None
        #     while cur:
        #         if to_point:
        #             to_point.next = cur.left or cur.right
        #         if cur.left:
        #             cur.left.next = cur.right
        #         to_point = cur.right or cur.left or to_point
        #         cur = cur.next
        #     while root:
        #         if root.left or root.right:
        #             root = root.left or root.right
        #             break
        #         root = root.next
        # return saveroot

        # A more clever way using sentinel
        sentinel = tail = Node(0)
        saveroot = root
        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next = root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail = sentinel
                root = sentinel.next
        return saveroot


Solution().connect(create_tree(Node, [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15]]))
