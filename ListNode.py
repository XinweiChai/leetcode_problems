class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        print(self.val)
        if self.next:
            self.next.print_all()


def create_list(*args):
    sentinel = ListNode(0)
    head = sentinel
    for i in args:
        head.next = ListNode(i)
        head = head.next
    return sentinel.next
