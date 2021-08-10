from collections import defaultdict


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dct = {}
        self.max_freq = 0
        self.min_freq = 0
        self.freq = defaultdict(set)

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.dct:
            key_freq = self.dct[key]
            self.freq[key_freq].remove(key)
            if self.min_freq == key_freq and not self.freq[key_freq]:
                self.min_freq += 1
            if self.max_freq == key_freq:
                self.max_freq += 1
            self.dct[key] += 1
        else:
            if not self.dct:
                self.max_freq = 1
            self.dct[key] = 1
            self.min_freq = 1
        self.freq[self.dct[key]].add(key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        key_freq = self.dct[key]
        self.freq[key_freq].remove(key)
        if self.max_freq == key_freq and not self.freq[key_freq]:
            self.max_freq -= 1
        if self.min_freq == key_freq:
            if self.min_freq != 1:
                self.min_freq -= 1
            elif not self.freq[1]:
                self.min_freq = 0
        if self.dct[key] == 1:
            self.dct.pop(key)
        else:
            self.dct[key] -= 1
            self.freq[self.dct[key]].add(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.dct:
            return ""
        temp = self.freq[self.max_freq].pop()
        self.freq[self.max_freq].add(temp)
        return temp

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if not self.dct:
            return ""
        temp = self.freq[self.min_freq].pop()
        self.freq[self.min_freq].add(temp)
        return temp


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
operators = ["inc", "inc", "inc", "inc", "inc", "inc", "dec", "dec", "getMinKey", "dec", "getMaxKey", "getMinKey"]
operands = [["a"], ["b"], ["b"], ["c"], ["c"], ["c"], ["b"], ["b"], [], ["a"], [], []]
for i, j in zip(operators, operands):
    print(eval('obj.' + i)(*j))
