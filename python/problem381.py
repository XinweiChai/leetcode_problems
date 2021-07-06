import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.dct = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.lst.append(val)
        self.dct[val] = self.dct.get(val, set()) | {len(self.lst) - 1}
        return len(self.dct[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.dct:
            pos = self.dct[val].pop()
            last_val = self.lst[-1]
            self.dct[last_val].add(pos)
            self.dct[last_val].remove(len(self.lst) - 1)
            if not self.dct[val]:
                self.dct.pop(val)
            self.lst[pos] = last_val
            self.lst.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.lst)


if __name__ == '__main__':
    # Your RandomizedCollection object will be instantiated and called as such:
    # param_1 = obj.insert(val)
    # param_2 = obj.remove(val)
    # param_3 = obj.getRandom()
    func_list = ["insert", "remove", "insert"]
    param_list = [[1], [1], [1]]
    obj = RandomizedCollection()
    for i, j in zip(func_list, param_list):
        eval('obj.' + i)(*j)
