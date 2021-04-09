from ListNode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        sentinel = ListNode(0, head)
        l = sentinel
        for _ in range(left - 1):
            l = l.next
        prev = l
        r = l.next
        for _ in range(right - left):
            r.next, r, prev = prev, r.next, r
        l.next.next = r.next
        l.next = r
        r.next = prev
        return sentinel.next


print(Solution().reverseBetween(ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5))))), 2,
                                4))
