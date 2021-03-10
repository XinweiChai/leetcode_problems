# Definition for singly-linked list.
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
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
        sentinel = ListNode()
        head = sentinel
        q = PriorityQueue()
        for index, i in enumerate(lists):
            if i:
                q.put((i.val, index, i))
        while not q.empty():
            _, index, head.next = q.get()
            head = head.next
            if head.next:
                q.put((head.next.val, index, head.next))
        return sentinel.next


a = ListNode(1, next=ListNode(4, next=ListNode(5)))
b = ListNode(1, next=ListNode(3, next=ListNode(4)))
c = ListNode(2, next=ListNode(6))
l = [a, b, c]
print(Solution().mergeKLists(l))
