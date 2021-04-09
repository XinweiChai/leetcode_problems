# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head: Node) -> Node:
        # Stupid deep copy
        # if not head:
        #     return None
        #
        # node_list = [head]
        # new_node = Node(head.val)
        # new_node_list = [new_node]
        # while head.next:
        #     node_list.append(head.next)
        #     new_node.next = Node(head.next.val)
        #     new_node_list.append(new_node.next)
        #     head = head.next
        #     new_node = new_node.next
        # for i in range(len(node_list)):
        #     if node_list[i].random:
        #         new_node_list[i].random = new_node_list[node_list.index(node_list[i].random)]
        #
        # return new_node_list[0]

        # Clever one
        # Insert duplicated nodes between original list
        if not head:
            return None
        save_head = head
        while head:
            new_head = Node(head.val)
            temp = head.next
            head.next = new_head
            new_head.next = temp
            head = temp

        save_new_head = save_head.next
        head = save_head

        # Copy random links
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next

        # Separate the duplicate one from original
        head = save_head
        new_head = save_new_head
        while head:
            head.next = new_head.next
            if head.next:
                new_head.next = head.next.next
            head = head.next
            new_head = new_head.next
        return save_new_head
