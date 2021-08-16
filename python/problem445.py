# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from python.ListNode import ListNode, create_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def length(ln):
            cnt = 0
            while ln:
                ln = ln.next
                cnt += 1
            return cnt

        len1 = length(l1)
        len2 = length(l2)
        if len2 > len1:
            l1, len1, l2, len2 = l2, len2, l1, len1

        def add(ln1, ln2, cnt):
            if not ln1:
                return 0
            if cnt:
                ln1.val += add(ln1.next, ln2, cnt - 1)
            else:
                ln1.val += ln2.val + add(ln1.next, ln2.next, 0)
            if ln1.val >= 10:
                ln1.val -= 10
                return 1
            return 0

        if add(l1, l2, len1 - len2):
            return ListNode(1, next=l1)
        return l1


if __name__ == '__main__':
    Solution().addTwoNumbers(create_list(9, 9, 9, 9), create_list(1)).print_all()
