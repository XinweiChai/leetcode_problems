from ListNode import ListNode, create_list


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


Solution().deleteDuplicates(create_list(1, 2, 3, 4, 4, 5)).print_all()
