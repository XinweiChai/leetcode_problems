# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def rec(count, head):
            if head.next:
                len_list = rec(count + 1, head.next)
            else:
                len_list = count
            if n != len_list and count + n == len_list:
                head.next = head.next.next
            return len_list

        len_list = rec(1, head)
        if n == len_list:
            return head.next
        return head
