from ListNode import ListNode, create_list


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


Solution().reverseBetween(create_list(1, 2, 3, 4, 5), 2, 4).print_all()
