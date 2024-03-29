from ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iterative
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        # Recursive
        if not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
