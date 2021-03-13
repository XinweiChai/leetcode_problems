import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx = self.pos[val]
            self.pos[self.nums[-1]] = idx
            self.pos.pop(val)
            self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return (self.nums[random.randrange(len(self.nums))])


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(0))
print(obj.insert(1))
print(obj.remove(0))
print(obj.insert(2))
print(obj.remove(1))
print(obj.getRandom())
