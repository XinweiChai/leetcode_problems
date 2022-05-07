from typing import Sequence
from ListNode import ListNode, create_list
from queue import PriorityQueue
import heapq


class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     sentinel = ListNode()
    #     head = sentinel
    #     while l1 and l2:
    #         if l1.val > l2.val:
    #             head.next = l2
    #             l2 = l2.next
    #         else:
    #             head.next = l1
    #             l1 = l1.next
    #         head = head.next
    #     head.next = l1 or l2
    #     return sentinel.next

    def mergeKLists(self, lists: Sequence[ListNode]) -> ListNode:
        # Stupid solution: merge one by one
        # cur = lists[0]
        # for i in range(1, len(lists)):
        #     cur = self.mergeTwoLists(cur,lists[i])
        # return cur

        # Use priorityQueue
        # if not lists:
        #     return None
        # sentinel = ListNode()
        # head = sentinel
        # lists = [i for i in lists if i]
        # if not lists:
        #     return None
        # lists.sort(key=lambda x: x.val)
        #
        # def insert_to_list(left, right):
        #     if left == right - 1:
        #         lists.insert(left + 1, head.next)
        #     else:
        #         mid = (left + right) // 2
        #         if head.next.val > lists[mid].val:
        #             insert_to_list(mid, right)
        #         else:
        #             insert_to_list(left, mid)
        #
        # while len(lists)>1:
        #     head.next = lists.pop(0)
        #     head = head.next
        #     if head.next:
        #         if head.next.val >= lists[-1].val:
        #             lists.insert(len(lists), head.next)
        #         elif head.next.val <= lists[0].val:
        #             lists.insert(0, head.next)
        #         else:
        #             insert_to_list(0, len(lists) - 1)
        # head.next = lists[0]
        # return sentinel.next

        # Use priorityQueue in python
        # sentinel = ListNode()
        # head = sentinel
        # q = PriorityQueue()
        # for index, i in enumerate(lists):
        #     if i:
        #         q.put((i.val, index, i))
        # while not q.empty():
        #     _, index, head.next = q.get()
        #     head = head.next
        #     if head.next:
        #         q.put((head.next.val, index, head.next))
        # return sentinel.next

        # Using equivalent heap, faster
        sentinel = ListNode()
        head = sentinel
        q = []
        for index, i in enumerate(lists):
            if i:
                heapq.heappush(q, (i.val, index, i))
        while q:
            _, index, head.next = heapq.heappop(q)
            head = head.next
            if head.next:
                heapq.heappush(q, (head.next.val, index, head.next))
        return sentinel.next


a = create_list(1, 4, 5)
b = create_list(1, 3, 4)
c = create_list(2, 6)
l = [a, b, c]
Solution().mergeKLists(l).print_all()
