# Definition for singly-linked list.
from dis import dis


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        print(self.val)
        if self.next:
            self.next.print_all()


class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = save_head = head

        while True:
            count = 0
            while head and count < k:  # use r to locate the range
                head = head.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = head, save_head
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, save_head = pre, save_head, head  # connect two k-groups
            else:
                return dummy.next


Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), 3).print_all()
