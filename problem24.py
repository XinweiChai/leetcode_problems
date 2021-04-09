from ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = head
        if head.next:
            new_head = head.next
            head.next = new_head.next
            new_head.next = head
        while head.next and head.next.next:
            temp = head.next
            temp2 = head.next.next.next
            head.next = head.next.next
            head.next.next = temp
            temp.next = temp2
            head = temp
        return new_head


a = ListNode(5)
b = ListNode(4, a)
c = ListNode(3, b)
d = ListNode(2, c)
e = ListNode(1, d)
Solution().swapPairs(e).print_all()
