# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        list_left = ListNode(201)
        list_right = ListNode(201)
        sentinel_left = list_left
        sentinel_right = list_right
        while head:
            if head.val < x:
                list_left.next = ListNode(head.val)
                list_left = list_left.next
            else:
                list_right.next = ListNode(head.val)
                list_right = list_right.next
            head = head.next
        list_left.next = sentinel_right.next
        return sentinel_left.next