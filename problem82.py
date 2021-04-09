from ListNode import ListNode


class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(101, head)
        pred = sentinel
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = head
            head = head.next
        return sentinel.next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
Solution().deleteDuplicates(a).print_all()
