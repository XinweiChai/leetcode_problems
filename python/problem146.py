from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.cache = {}
        self.next, self.pred = {}, {}
        self.head, self.tail = '#', '$'
        self.connect(self.head, self.tail)

    def connect(self, a, b):
        self.next[a], self.pred[b] = b, a

    def delete(self, key):
        self.connect(self.pred[key], self.next[key])
        del self.pred[key], self.next[key], self.cache[key]

    def append(self, k, v):
        self.cache[k] = v
        self.connect(self.pred[self.tail], k)
        self.connect(k, self.tail)
        if len(self.cache) > self.size:
            self.delete(self.next[self.head])

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)
        return val

    def put(self, key, value):
        if key in self.cache:
            self.delete(key)
        self.append(key, value)


class LRUCache2(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key, last=True)
            return self[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key, last=True)

        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)


x = LRUCache(2)
print(x.put(1, 1))
print(x.put(2, 2))
print(x.get(1))
print(x.put(3, 3))
print(x.get(2))
print(x.put(4, 4))
print(x.get(1))
print(x.get(3))
print(x.get(4))
