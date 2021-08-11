class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}, next: {self.next.val if self.next else None}'

    def print_all(self):
        print(self.val)
        if self.next:
            self.next.print_all()


def create_list(*args) -> ListNode:
    sentinel = ListNode(0)
    head = sentinel
    # if isinstance(args[0], list):
    if type(args[0]) == list:
        args = args[0]
    for i in args:
        head.next = ListNode(i)
        head = head.next
    return sentinel.next
