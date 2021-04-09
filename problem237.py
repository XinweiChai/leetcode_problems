from ListNode import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        """
        Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
