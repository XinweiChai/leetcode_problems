from ListNode import ListNode, create_list


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        sentinel = ListNode(next=head)
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        line2 = slow.next
        slow.next = None

        cur = line2
        prev = None
        while cur:
            # succ = cur.next
            # cur.next = prev
            # prev = cur
            # cur = succ

            # Concise notation
            cur.next, prev, cur = prev, cur, cur.next
        line2 = prev

        while line2:
            # temp = line2.next
            # line2.next = head.next
            # head.next = line2
            # head = head.next.next
            # line2 = temp

            # Concise notation
            line2.next, head.next, head, line2 = head.next, line2, head.next, line2.next
        sentinel.print_all()


if __name__ == '__main__':
    Solution().reorderList(create_list(1, 2, 3, 4, 5))
