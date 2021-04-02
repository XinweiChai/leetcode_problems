class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def find_mid_pointers(node, n):
    if not node or n <= 0:
        return []
    p_fast = node
    p_start = node
    cnt = 0
    ans = [None] * n

    while p_fast and p_fast.next:
        p_fast = p_fast.next.next
    if cnt >= n // 2:
        p_start = p_start.next
    cnt += 1
    for i in range(n):
        if p_start:
            ans[i] = p_start
            p_start = p_start.next
    return ans

x = find_mid_pointers(Node(1,Node(2,Node(3))),4)

y=1