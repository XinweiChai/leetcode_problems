"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        stack = []
        save_head = head
        while head or stack:
            if not head:
                head = stack.pop()
                prev.next = head
                head.prev = prev
            elif head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.child = None

            if head.next:
                head.next.prev = head
            prev = head
            head = head.next
        return save_head

    # A clearer solution
    def flatten2(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dummy = Node(0, None, head, None)
        stack = [head]
        prev = dummy

        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root

            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root

        dummy.next.prev = None
        return dummy.next