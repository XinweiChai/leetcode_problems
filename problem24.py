from ListNode import ListNode, create_list


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


a = create_list([1, 2, 3, 4, 5])
Solution().swapPairs(a).print_all()
