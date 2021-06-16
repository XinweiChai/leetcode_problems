from collections import deque


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        q2 = deque()
        while self.q:
            q2.append(self.q.pop())
        self.q.append(x)
        while q2:
            self.q.append(q2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.q.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(self.q)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()