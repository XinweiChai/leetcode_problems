from ListNode import ListNode, create_list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        init = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return init

if __name__ == '__main__':
    print(Solution().deleteDuplicates(create_list(1, 2, 3, 3, 4, 4, 5)))
