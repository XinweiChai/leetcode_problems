# Very slow
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_freq = {}
        self.freq_key = {}
        self.pred = {-1: 0}
        self.succ = {0: -1}

    def insert(self, idx, freq, direction=1):
        if direction == -1:
            self.insert(self.pred[idx], freq, -direction)
        else:
            temp = self.succ[idx]
            self.succ[idx] = freq
            self.succ[freq] = temp
            self.pred[temp] = freq
            self.pred[freq] = idx

    def remove(self, freq):
        self.succ[self.pred[freq]] = self.succ[freq]
        self.pred[self.succ[freq]] = self.pred[freq]
        self.succ.pop(freq)
        self.pred.pop(freq)

    def move(self, freq, direction=1):
        self.insert(freq - direction, freq, direction)
        self.remove(freq - direction)

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.key_freq[key] = self.key_freq.get(key, 0) + 1
        curr_freq = self.key_freq[key]
        self.freq_key[curr_freq] = self.freq_key.get(curr_freq, set()) | {key}
        if curr_freq != 1 and len(self.freq_key[curr_freq - 1]) == 1:
            self.freq_key.pop(curr_freq - 1)
            if curr_freq not in self.succ:
                self.move(curr_freq)
            else:
                self.remove(curr_freq - 1)
        else:
            self.freq_key.get(curr_freq - 1, set()).discard(key)
            if curr_freq not in self.succ:
                self.insert(curr_freq - 1, curr_freq)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        self.key_freq[key] -= 1
        curr_freq = self.key_freq[key]
        if curr_freq != 0:
            self.freq_key[curr_freq] = self.freq_key.get(curr_freq, set()) | {key}
        else:
            self.key_freq.pop(key)
        if len(self.freq_key[curr_freq + 1]) == 1:
            self.freq_key.pop(curr_freq + 1)
            if curr_freq not in self.succ:
                self.move(curr_freq, -1)
            else:
                self.remove(curr_freq + 1)
        else:
            self.freq_key[curr_freq + 1].remove(key)
            if curr_freq not in self.succ:
                self.insert(curr_freq + 1, curr_freq, -1)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        max_freq = self.pred[-1]
        if max_freq == 0:
            return ""
        key = self.freq_key[max_freq].pop()
        self.freq_key[max_freq].add(key)
        return key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        min_freq = self.succ[0]
        if min_freq == -1:
            return ""
        key = self.freq_key[min_freq].pop()
        self.freq_key[min_freq].add(key)
        return key


# A clever solution defining node and map strings to nodes
class Node:
    def __init__(self, key, v) -> None:
        self.key = key
        self.count = v
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        return f'({self.key}: {self.count})'


def swap_with_prev(c):
    # swap up: A B C D to A C B D
    # print(f'swap {b}{c}')
    b = c.prev
    a = b.prev
    d = c.next
    a.next = c
    c.prev = a
    c.next = b
    b.prev = c
    d.prev = b
    b.next = d


class AllOne2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}
        self.head = Node('', 5e4)
        self.tail = Node('', -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.m:
            n = Node(key, 1)
            # insert node
            self.tail.prev.next = n
            n.prev = self.tail.prev
            n.next = self.tail
            self.tail.prev = n
            self.m[key] = n
        else:
            n = self.m[key]
            n.count += 1
            while n.count > n.prev.count:
                swap_with_prev(n)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        n = self.m[key]
        n.count -= 1
        if n.count <= 0:
            # delete node
            n.prev.next = n.next
            n.next.prev = n.prev
            self.m.pop(key)
        elif n.count < n.next.count:
            swap_with_prev(n.next)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.head.next.key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.tail.prev.key


# With some cheating
class AllOne3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = {}
        self.cacheMin = None
        self.cacheMax = None

    def clearCache(self):
        self.cacheMin = None
        self.cacheMax = None

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        self.clearCache()
        self.storage[key] = self.storage.get(key, 0) + 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        self.clearCache()
        reduce = self.storage[key] - 1
        if reduce == 0:
            del self.storage[key]
        else:
            self.storage[key] = reduce

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.cacheMax:
            return self.cacheMax

        if not self.storage:
            self.cacheMax = ""
        else:
            self.cacheMax = max(self.storage, key=self.storage.get)
        return self.cacheMax

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.cacheMin:
            return self.cacheMin
        if not self.storage:
            self.cacheMin = ""
        else:
            self.cacheMin = min(self.storage, key=self.storage.get)
        return self.cacheMin

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


# Your AllOne object will be instantiated and called as such:
obj = AllOne3()
operators = ["inc", "inc", "inc", "inc", "inc", "inc", "dec", "dec", "getMinKey", "dec", "getMaxKey", "getMinKey"]
operands = [["a"], ["b"], ["b"], ["c"], ["c"], ["c"], ["b"], ["b"], [], ["a"], [], []]
for i, j in zip(operators, operands):
    print(eval('obj.' + i)(*j))
