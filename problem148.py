# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
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
        #     # Quicksort, we can only choose the first element as pivot, we might encounter the case of O(n^2)
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
        #
        # # Mergesort, Top-down recursion uses O(logn) space
        # def merge(self, h1, h2):
        #     dummy = tail = ListNode(None)
        #     while h1 and h2:
        #         if h1.val < h2.val:
        #             tail.next, tail, h1 = h1, h1, h1.next
        #         else:
        #             tail.next, tail, h2 = h2, h2, h2.next
        #
        #     tail.next = h1 or h2
        #     return dummy.next
        #
        # def sortList(self, head):
        #     if not head or not head.next:
        #         return head
        #
        #     pre, slow, fast = None, head, head
        #     while fast and fast.next:
        #         pre, slow, fast = slow, slow.next, fast.next.next
        #     pre.next = None
        #
        #     return self.merge(*map(self.sortList, (head, slow)))
        #     # Equivalent to:
        #     x = self.sortList(head)
        #     y = self.sortList(slow)
        #     return self.merge(x,y)

        # Mergesort, bottom-up iteration, using O(1) space
        if not head or not head.next: return head

        def getSize(head):
            # Simply count the length of linked list
            counter = 0
            while head:
                counter += 1
                head = head.next
            return counter

        def split(head, size):
            # given the head & size, return the the start node of next chunk
            for i in range(size - 1):
                if not head:
                    break
                head = head.next

            if not head: return None
            next_start, head.next = head.next, None  # disconnect

            return next_start

        def merge(l1, l2, dummy_start):
            # Given dummy_start, merge two lists, and return the tail of merged list
            curr = dummy_start
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next

            curr.next = l1 if l1 else l2
            while curr.next: curr = curr.next  # Find tail
            # the returned tail should be the "dummy_start" node of next chunk
            return curr

        total_length = getSize(head)
        dummy = ListNode(0)
        dummy.next = head
        start, dummy_start, size = None, None, 1

        while size < total_length:
            dummy_start = dummy
            start = dummy.next
            while start:
                left = start
                right = split(left, size)  # start from left, cut with size=size
                start = split(right, size)  # start from right, cut with size=size
                dummy_start = merge(left, right, dummy_start)  # returned tail = next dummy_start
            size *= 2
        return dummy.next


a = ListNode(10, next=ListNode(1, next=ListNode(30, next=ListNode(2, next=ListNode(5)))))
b = Solution().sortList(a)
c = 1
