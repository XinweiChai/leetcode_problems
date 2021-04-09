from ListNode import ListNode


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add_one = False
        sum_node = ListNode(0)
        savehead = sum_node
        while l1 or l2 or add_one:
            sum_node.next = ListNode(0)
            sum_node = sum_node.next
            if l1:
                sum_node.val += l1.val
                l1 = l1.next
            if l2:
                sum_node.val += l2.val
                l2 = l2.next
            if add_one:
                sum_node.val += 1
                add_one = False
            if sum_node.val >= 10:
                sum_node.val -= 10
                add_one = True
        return savehead.next


b = Solution().addTwoNumbers(ListNode(2, next=ListNode(4, next=ListNode(3, next=ListNode(5)))),
                             ListNode(5, next=ListNode(6, next=ListNode(4))))
x = 1
