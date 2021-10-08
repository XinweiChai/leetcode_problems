class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.cirQ = [None] * k
        self.front = 0
        self.rear = 0
        self.full = False
        self.empty = True

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cirQ[self.rear] = value
        self.rear += 1
        self.empty = False
        if self.rear == self.size:
            self.rear -= self.size
        if self.rear == self.front:
            self.full = True
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front += 1
        self.full = False
        if self.front == self.size:
            self.front -= self.size
        if self.front == self.rear:
            self.empty = True
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cirQ[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cirQ[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.empty

    def isFull(self) -> bool:
        # return self.rear - self.front == self.size
        return self.full

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


if __name__ == '__main__':
    operators = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    operands = [[3], [1], [2], [3], [4], [], [], [], [4], []]
    for idx, (i, j) in enumerate(zip(operators, operands)):
        if idx == 0:
            obj = eval(f'{i}')(*j)
        else:
            print(eval(f'obj.{i}')(*j))
