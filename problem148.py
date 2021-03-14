# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def sortList(self, head: ListNode) -> ListNode:
    #     # Copy and sort
    #     if not head:
    #         return None
    #     elements = []
    #     while head:
    #         elements.append(head.val)
    #         head = head.next
    #     elements.sort()
    #     head = ListNode(elements[0])
    #     savehead = head
    #     for i in elements[1:]:
    #         head.next = ListNode(i)
    #         head = head.next
    #     return savehead
    #
    #     Quicksort, we can only choose the first element as pivot, we might encounter the case of O(n^2)
    #     if not head:
    #         return None
    #     sentinel = ListNode(next=head)
    #     count = 0
    #     while head:
    #         count += 1
    #         head = head.next
    #
    #     def qs(start_node, count):
    #         if count > 0:
    #             pivot = start_node.next
    #             last = pivot
    #             cur = last.next
    #             c_large = 0
    #             for i in range(count):
    #                 if cur.val < pivot.val:
    #                     last.next = cur.next
    #                     cur.next = start_node.next
    #                     start_node.next = cur
    #                     cur = last.next
    #                 else:
    #                     c_large += 1
    #                     cur = cur.next
    #                     last = last.next
    #             qs(start_node, count - 1 - c_large)
    #             qs(pivot, c_large - 1)
    #
    #     qs(sentinel, count - 1)
    #     return sentinel.next

    # Mergesort
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))


a = ListNode(5, next=ListNode(3, next=ListNode(3, next=ListNode(3, next=ListNode(3)))))
b = Solution().sortList(a)
c = 1
