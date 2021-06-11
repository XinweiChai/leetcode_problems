from ListNode import ListNode, create_list


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(next=head)
        cur = sentinel
        while cur:
            if cur.next and cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return sentinel.next


if __name__ == '__main__':
    Solution().removeElements(create_list(7, 7, 7, 7), 7).print_all()
