from ListNode import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        tortoise = hare = head
        while hare.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                tortoise = head
                while tortoise != hare:
                    tortoise = tortoise.next
                    hare = hare.next
                return tortoise
        return None
