from ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # def rec(count, node):
        #     if node.next:
        #         len_list = rec(count + 1, node.next)
        #     else:
        #         len_list = count
        #     if n != len_list and count + n == len_list:
        #         node.next = node.next.next
        #     return len_list
        #
        # len_list = rec(1, head)
        # if n == len_list:
        #     return head.next
        # return head

        # Iterative
        sentinel = ListNode(next=head)
        for _ in range(n):
            head = head.next
        another = sentinel
        while head:
            head = head.next
            another = another.next
        another.next = another.next.next
        return sentinel.next
