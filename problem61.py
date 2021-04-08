# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        sentinel = ListNode(0, head)
        l = 1
        while head.next:
            l += 1
            head = head.next
        k = k % l
        head.next = sentinel.next
        for i in range(l - k):
            head = head.next
        sentinel.next = head.next
        head.next = None
        return sentinel.next
