from ListNode import ListNode


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
